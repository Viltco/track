# -*- coding: utf-8 -*-

from odoo import fields, models


class SaleReport(models.Model):
    _inherit = "sale.report"

    sale_region_id = fields.Many2one(comodel_name="sale.region", string="Region")
    vehicle_number_ids = fields.Many2many(comodel_name="vehicle.number", string="Vehicle Number")
    technician_id = fields.Many2one(comodel_name="res.partner", string="Technician")

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        fields['sale_region_id'] = ", s.sale_region_id"
        # fields['technician_id'] = ", s.technician_id"
        groupby += ', s.sale_region_id'
        # groupby += ', s.technician_id'
        return super(SaleReport, self)._query(
            with_clause, fields, groupby, from_clause
        )

    def _select(self):
        return super(SaleReport, self)._select() + ", s.sale_region_id"

    def _group_by(self):
        return super(SaleReport, self)._group_by() + ", s.sale_region_id"
