# -*- coding: utf-8 -*-
{
    'name': "Show Fallback Pricelist in Contacts",
    'summary': """Show main pricelist on partner form (fallback pricelist)""",
    'depends': ['base', 'product', 'sale', 'crm'],
    'data': [
        'views/partner_w_plist.xml'
    ],
    'version' : "1.0",
    'images': ['images/thumbnail.png'],
    'author' : "Piotr Cierkosz",
    'installable' : True,
    'description' : "This module adds Fallback pricelist to the Customer View.",
    'website': "www.cier.tech",
    'category': 'Extra Tools',
    'license': 'Other proprietary',
    'price': 9.0,
    'currency': 'EUR',
}
