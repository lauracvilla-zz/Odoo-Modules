# -*- coding: utf-8 -*-

from openerp import api, fields, models, _

class client_order_ref_stock(models.Model):
# where to place new fields
    _inherit = 'stock.picking'
# getting country code to the accounting model
    client_order_ref = fields.Char(related="sale_id.client_order_ref")
