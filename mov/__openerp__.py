# -*- coding: utf-8 -*-
{
    'name': "Minimum Order Value",
    'summary': """
        Minimum order value - useful hint for purchasing department
    """,
    'description' : "Minimum order value - useful hint for purchasing department",
    'depends': ['base', 'sale', 'purchase' ],
    'data': [
        'views/mov_partner_form.xml','views/mov_purchase_form.xml'
    ],
    'version': '1.0',
    'images': ['images/thumbnail.png'],
    'author' : "Piotr Cierkosz",
    'category': 'Purchases',
    'license': 'Other proprietary',
    'website': "https://www.cier.tech",
    'price': 10.0,
    'currency': 'EUR',
    'installable' : True,
}
