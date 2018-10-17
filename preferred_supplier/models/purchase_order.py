# -*- coding: utf-8 -*-

from openerp import models, fields, api

class pucrhase_order_pref_supplier(models.Model):
    _inherit = 'purchase.order.line'
#this field will be displayed on the product list in the purchase order
    preferred_supplier = fields.Char(related="product_id.preferred_supplier_middle", string="Preferred Supplier", readonly="true")
