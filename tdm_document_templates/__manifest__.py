# -*- coding: utf-8 -*-
{
    'name': 'Financial Document Templates',
    'version': '1.1',
    'category': 'Sales',
    'sequence': 2,
    'author': "Sidath Liyanage",
    'website': '',
    'summary': 'Financial document templates for TDM',
    'description': """Financial document templates for TDM""",
    'depends': ['base', 'account'],
    'data': [
        'data/report_data.xml',
        'views/report_invoice.xml',
        'views/report_order_confirmation.xml',
        # 'views/report_vendor_bill.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3'
}

