# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    sale_region_id = fields.Many2one(comodel_name="sale.region", string="Region")
    vehicle_number_ids = fields.Many2many(comodel_name="vehicle.number", string="Vehicle Number")
    technician_ids = fields.Many2many(comodel_name="res.partner", string="Technician")


class StockMove(models.Model):
    _inherit = 'stock.move'

    def _get_new_picking_values(self):
        res = super(StockMove, self)._get_new_picking_values()
        res.update({'sale_region_id': self.group_id.sale_id.sale_region_id.id,
                    'vehicle_number_ids': self.group_id.sale_id.vehicle_number_ids.ids,
                    'technician_ids': self.group_id.sale_id.technician_ids.ids,
                    })
        return res