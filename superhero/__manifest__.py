# -*- coding: utf-8 -*-
{
    'name': "superhero",

    'summary': """
        Superhero Exercise by CPTI Joseph""",

    'description': """
        Custom app on top of POS App
    """,

    'author': "Courtesy Point",
    'website': "http://www.courtesypoint.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales/Point of Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','point_of_sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/superhero_menus.xml',
        'views/superhero_views.xml',
        'views/pos_config_views.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/popular_superheroes_template.xml',
        'report/report.xml',
        'wizard/popular_superhero_wizard_view.xml',
    ],
    # Test
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': 'true',
}
