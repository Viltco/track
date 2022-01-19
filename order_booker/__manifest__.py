# -*- coding: utf-8 -*-
{
    'name': "Order Booker",
    'description': "Order book in Sale, Accounting and Crm",
    'author': 'SolutionFounder',
    'website': "http://www.solutionfounder.com",
    'category': 'Sale',
    'version': '14.0.1.0.2',
    'depends': ['base', 'sale_management', 'account_accountant', 'crm'],
    'data': [
        'views/res_partner.xml',
        'views/sale_order.xml',
        'views/account_move.xml',
        'views/crm_lead.xml',
             ],
    'installable': True,
    'application': False,
    'auto_install': False,
}