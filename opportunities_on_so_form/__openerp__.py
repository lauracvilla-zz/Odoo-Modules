# -*- coding: utf-8 -*-
# For more information and help please contact author. www.cierkosz.com, www.cier.website_product_attachment_shop

{
    'name' : "Opportunity on Sales Orders form",
    'version' : "1.0",
    'images': ['images/thumbnail.png'],
    'author' : "Piotr Cierkosz",
    'category': 'Sales',
    'license': 'Other proprietary',
    'summary': 'This module allows every user to see the connected opportunity on the sales order and quotation form',
    'price': 5.0,
    'currency': 'EUR',
    'depends' : ['sale', 'crm'],
    'installable' : True,
    'description' : "This module activates the Reporting view with Opportunities on the Sales Orders Form (Sales / Sales Orders / Other Information). It also applies to Quotations. It simply updates the treee view in Sales/Sales Orders and Sales/Quotations.",
    'website' : "www.cier.tech",
    'data': ['views/so_views.xml',],

}
