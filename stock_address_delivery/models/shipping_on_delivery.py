# -*- coding: utf-8 -*-

from openerp import api, fields, models

class ShippingOnDelivery(models.Model):
# where to place new fields
    _inherit = 'stock.picking'
# getting user_id to the stock picking
    partner_shipping_id = fields.Many2one(
        'res.partner', 'Shipping Address', help="Change the address only if different than in Sales Order",
        states={'done': [('readonly', True)], 'cancel': [('readonly', True)]})
