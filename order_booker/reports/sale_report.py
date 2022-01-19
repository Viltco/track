# -*- coding: utf-8 -*-

from odoo import fields, models


class SaleReport(models.Model):
    _inherit = "sale.report"

    order_booker_id = fields.Many2one('res.partner', string='Order Booker')

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        fields['order_booker_id'] = ", s.order_booker_id"
        groupby += ', s.order_booker_id'
        return super(SaleReport, self)._query(
            with_clause, fields, groupby, from_clause
        )

    def _select(self):
        return super(SaleReport, self)._select() + ", s.order_booker_id"

    def _group_by(self):
        return super(SaleReport, self)._group_by() + ", s.order_booker_id"
