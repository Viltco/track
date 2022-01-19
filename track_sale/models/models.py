# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sale_lot_ids = fields.Many2many('stock.production.lot')
    sale_lot_ids_new = fields.Many2many('stock.production.lot', compute='compute_sin_lots')
    do_count = fields.Integer(compute='compute_do')

    def compute_do(self):
        count = self.env['stock.picking'].search_count([('origin', '=', self.name)])
        self.do_count = count

    @api.depends('sale_lot_ids')
    def compute_sin_lots(self):
        lots = self.env['stock.production.lot'].search([('product_id.categ_id.name', '=', 'Sim')])
        self.sale_lot_ids_new = lots.ids

    def action_view_do(self):
        return {
            'name': 'Delivery Order',
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'stock.picking',
            'domain': [('origin', '=', self.name)],
        }

    def action_confirm(self):
        record = super(SaleOrder, self).action_confirm()
        if self.sale_lot_ids:
            self.create_delivery()
        return record

    def create_delivery(self):
        picking_type_id = self.env['stock.picking.type'].search([('code', '=', 'outgoing')], limit=1)
        # warehouse = self.env['stock.location'].search([('name', '=', 'Stock')])
        warehouse = self.picking_ids[0].location_id
        line_vals = []
        for line in self.sale_lot_ids:
            line_vals.append((0, 0, {
                'product_id': line.product_id.id,
                'name': line.product_id.name,
                'product_uom': line.product_id.uom_id.id,
                'location_id': warehouse.id,
                'location_dest_id': self.partner_id.property_stock_customer.id,
                'product_uom_qty': 1,
                # 'quantity_done': line.qty_done,
            }))
        new_picking = {
            'move_lines': line_vals,
            'picking_type_id': picking_type_id.id,
            'state': 'draft',
            'origin': self.name,
            'sale_id': self.id,
            'location_id': warehouse.id,
            'location_dest_id': self.partner_id.property_stock_customer.id}

        picking = self.env['stock.picking'].create(new_picking)

        # new_picking.action_confirm()
        # new_picking.action_assign()
        # new_picking.button_validate()
