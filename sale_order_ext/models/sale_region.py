# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class SaleRegion(models.Model):
    _name = 'sale.region'
    _description = 'Sale Region'

    name = fields.Char(string="Name", required=True)

    _sql_constraints = [
        ('unique_name', 'unique (name)', 'Name already exists')
    ]

    def unlink(self):
        for rec in self:
            sale_obj = self.env['sale.order']
            obj = sale_obj.search([('sale_region_id', '=', rec.id)])
            if obj:
                raise UserError(_("You are trying to delete a Region that is still used in Sale Order!"))
            return super(SaleRegion, rec).unlink()
