# -*- coding: utf-8 -*-
{
    'name': "Preferred supplier of stock",
    'author': "Piotr Cierkosz",
    'website': "https://www.cier.tech",
    'category': 'Purchase',
    'version': '1.0',
    'depends': ['sale', 'sale_stock', 'product', 'purchase' ],
    'data': [
        'views/product_template_pref_supp.xml',
        'views/purchase_order_pref_supp.xml',
    ],
    'images': ['images/thumbnail.png'],
    'license': 'Other proprietary',
    'summary': 'Set a preferred supplier against the product variants',
    'price': 15.0,
    'currency': 'EUR',
    'installable' : True,
    'description' : "Set a preferred supplier against the product variants",
    'live_test_url': 'https://www.youtube.com/watch?v=rRD9lf1qaGc',
}
