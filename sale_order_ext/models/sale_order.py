# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    technician_ids = fields.Many2many(comodel_name="res.partner", string="Technician", required=True)
    sale_region_id = fields.Many2one(comodel_name="sale.region", string="Region", required=True)
    vehicle_number_ids = fields.Many2many(comodel_name="vehicle.number", string="Vehicle Number", required=True)
    no_of_vehicle = fields.Integer(string="No of Vehicles", compute='compute_no_of_vehicles', store=True)
    round_off = fields.Boolean(string="Round off")

    @api.depends('order_line.price_total', 'round_off')
    def _amount_all(self):
        """
        Compute the total amounts of the SO.
        """
        for order in self:
            amount_untaxed = amount_tax = 0.0
            for line in order.order_line:
                amount_untaxed += line.price_subtotal
                amount_tax += line.price_tax
            if order.round_off:
                order.update({
                    'amount_untaxed': round(5 + amount_untaxed)-5,
                    'amount_tax': round(5 + amount_tax)-5,
                    'amount_total': round(5 + (amount_untaxed + amount_tax))-5,
                })
            else:
                order.update({
                    'amount_untaxed': amount_untaxed,
                    'amount_tax': amount_tax,
                    'amount_total': amount_untaxed + amount_tax,
                })

    def data_for_required_fields(self):
        sale_orders = self.env['sale.order'].search([])
        for sale in sale_orders:
            if not sale.technician_id:
                sale.technician_id = 1
            if not sale.sale_region_id:
                sale.sale_region_id = 1
            if not sale.vehicle_number_ids:
                sale.vehicle_number_ids = [1]

    @api.depends('vehicle_number_ids')
    def compute_no_of_vehicles(self):
        for rec in self:
            count = 0
            for vehicle in rec.vehicle_number_ids:
                if vehicle.name != 'N/A':
                    count += 1
            rec.no_of_vehicle = count

    def _prepare_invoice(self):
        result = super(SaleOrder, self)._prepare_invoice()
        result['sale_region_id'] = self.sale_region_id.id if self.sale_region_id else False
        result['vehicle_number_ids'] = self.vehicle_number_ids.ids if self.vehicle_number_ids else False
        result['technician_ids'] = self.technician_ids.ids if self.technician_ids else False
        # result['round_off'] = self.round_off if self.round_off else False
        return result


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def get_sale_order_line_multiline_description_sale(self, product):
        result = super(SaleOrderLine, self).get_sale_order_line_multiline_description_sale(product)
        if not product.description:
            return result
        else:
            return product.description


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    def _create_invoice(self, order, so_line, amount):
        result = super(SaleAdvancePaymentInv, self)._create_invoice(order, so_line, amount)
        sale_order = self.env['sale.order'].search([('id', '=', self.env.context.get('active_id'))])
        result.sale_region_id = sale_order.sale_region_id.id if sale_order.sale_region_id else False
        result.vehicle_number_ids = sale_order.vehicle_number_ids.ids if sale_order.vehicle_number_ids else False
        result.technician_ids = sale_order.technician_ids.ids if sale_order.technician_ids else False
        return result