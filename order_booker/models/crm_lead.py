# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    order_booker_id = fields.Many2one(comodel_name="res.partner", string="Order Booker", required=False)

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        for rec in self:
            if rec.partner_id:
                rec.order_booker_id = rec.partner_id.order_booker_id
