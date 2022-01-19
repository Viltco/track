# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class VehicleNumber(models.Model):
    _name = 'vehicle.number'

    name = fields.Char(string="Vehicle Number", required=True)

    _sql_constraints = [
        ('unique_name', 'unique (name)', 'Name already exists')
    ]

    def unlink(self):
        for rec in self:
            sale_obj = self.env['sale.order']
            obj = sale_obj.search([('vehicle_number_ids', 'in', rec.id)])
            if obj:
                raise UserError(_("You are trying to delete a Vehicle Number that is still used in Sale Order!"))
            return super(VehicleNumber, rec).unlink()
