# -*- coding: utf-8 -*-
{
    'name': "Email Management",

    'summary': """
        A Module to create custom Buttons""",

    'description': """
        Module to create buttons that allow for redirection to other web pages 
    """,

    'author': "Kapital Banque",
    'website': "https://www.kapitalbanque.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Email_Redirection',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/test_menu.xml',
    ],
    'installable': True,
    'application': True,

}
