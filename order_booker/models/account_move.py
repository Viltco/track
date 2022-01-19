# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class AccountMove(models.Model):
    _inherit = 'account.move'

    order_booker_id = fields.Many2one(comodel_name="res.partner", string="Order Booker", required=False)

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        result = super(AccountMove, self)._onchange_partner_id()
        if self.move_type in ['out_invoice','out_refund','out_receipt']:
            values = {}
            if not self.partner_id:
                self.update({
                    'order_booker_id': False,
                })
                return
            partner_order_booker = self.partner_id.order_booker_id
            order_booker_id = partner_order_booker.id
            if order_booker_id:
                values['order_booker_id'] = order_booker_id
            self.update(values)
        return result