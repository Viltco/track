# -*- coding: utf-8 -*-
{
    'name': "Sale Order Extension",
    'description': "Sale Order Extension",
    'author': 'Techistan',
    'website': "http://www.techistan.com",
    'category': 'Sale',
    'version': '14.0.1.0.9',
    'application': True,
    'depends': ['base', 'sale_management', 'account_accountant', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner.xml',
        'views/sale_order.xml',
        'views/account_move.xml',
        'views/stock_picking.xml',
        'views/sale_region.xml',
        'views/vehicle_number.xml',
             ],
    'installable': True,
    'application': False,
    'auto_install': False,
}