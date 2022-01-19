# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    order_booker_id = fields.Many2one(comodel_name="res.partner", string="Order Booker", required=False)