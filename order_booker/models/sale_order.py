# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    order_booker_id = fields.Many2one(comodel_name="res.partner", string="Order Booker", required=False)

    @api.onchange('partner_id')
    def onchange_partner_shipping_id(self):
        result = super(SaleOrder, self).onchange_partner_shipping_id()
        if not self.partner_id:
            self.update({'order_booker_id': False})
            return
        partner_order_booker = self.partner_id.order_booker_id
        order_booker_id = partner_order_booker.id
        if order_booker_id:
            self.update({'order_booker_id': order_booker_id})
        return result

    def _prepare_invoice(self):
        result = super(SaleOrder, self)._prepare_invoice()
        result['order_booker_id'] = self.order_booker_id.id if self.order_booker_id else False
        return result