# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_technician = fields.Boolean(string="Is Technician")
    is_order_booker = fields.Boolean(string="Is Order Booker")
