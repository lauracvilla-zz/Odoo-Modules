# -*- coding: utf-8 -*-
# For more information and help please contact author. www.cierkosz.com, www.cier.website_product_attachment_shop
{
    'name' : "Opportunity on Sales Orders form",
    'version' : "1.1",
    'images': ['images/thumbnail.png'],
    'author' : "Piotr Cierkosz",
    'category': 'Sales',
    'license': 'Other proprietary',
    'summary': 'This module allows every user to see the connected opportunity on the sales order and quotation form',
    'price': 10.0,
    'currency': 'EUR',
    'depends' : ['sale_management', 'crm'],
    'installable' : True,
    'description' : "Module adds Opportunity field on Orders and Quotations fields. It also adds opportunity to the pdf (if there is any)",
    'website' : "www.cier.tech",
    'data': ['views/so_views.xml','views/opportunity_on_report.xml',],
}
