# -*- coding: utf-8 -*-

from openerp import models, fields, api, _
from openerp.tools import  float_compare
import openerp.addons.decimal_precision as dp

class product_middle_field(models.Model):
    _inherit = 'product.product'
# this field is copying the name value from preffered supplier
    preferred_supplier_middle = fields.Char(related="preferred_supplier.name", store="true", readonly="true")
