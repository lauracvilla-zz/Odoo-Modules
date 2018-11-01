# -*- coding: utf-8 -*-
{
    'name': 'Previous Invoice Number',
    'author': 'Piotr Cierkosz',
    'website': 'http://www.cierkosz.com',
    'version': '1.0',
    'category': 'Accounting',
    'installable': True,
    'auto_install': False,
    'license': 'Other proprietary',
    'images': ['images/thumbnail.png'],
    'demo': [],
    'depends': ['account'],
    'summary': 'Previous Invoice Number for easier transition to Odoo Accounting',
    'price': 15.0,
    'currency': 'EUR',
    'data': ['views/old_inv_inv.xml', 'views/old_inv_inv_tree.xml', 'views/old_inv_inv_purch.xml', 'views/old_inv_inv_tree_purch.xml', 'views/old_inv_inv_doc.xml'],
    'description': """
    Moving accounting to Odoo and want to map invoice numbers from old invoicing system?
    This module will allow you to:
    - save invoice numbers from other system and view them next to each other
    - display old invoice number in the printed Invoice(pdf) if exists so your customer will be able to map them
    - see the old invoice number on the tree view(list view) next to Odoo Invoice numbers
    """
}
