# -*- coding: utf-8 -*-

from odoo import fields, models


class SaleReport(models.Model):
    _inherit = "account.invoice.report"

    sale_region_id = fields.Many2one(comodel_name="sale.region", string="Region")
    # vehicle_number = fields.Char(string="Vehicle Number")
    # technician_id = fields.Many2one(comodel_name="res.partner", string="Technician", required=False)

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        fields['sale_region_id'] = ", move.sale_region_id"
        # fields['vehicle_number'] = ", move.vehicle_number"
        # fields['technician_id'] = ", move.technician_id"
        groupby += ', s.sale_region_id'
        # groupby += ', s.vehicle_number'
        # groupby += ', s.technician_id'
        return super(SaleReport, self)._query(
            with_clause, fields, groupby, from_clause
        )

    def _select(self):
        return super(SaleReport, self)._select() + ", move.sale_region_id"

    def _group_by(self):
        return super(SaleReport, self)._group_by() + ", move.sale_region_id"
