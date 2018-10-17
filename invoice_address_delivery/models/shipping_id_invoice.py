# -*- coding: utf-8 -*-

from openerp import api, fields, models, _

class Shipping_Invoice(models.Model):
# where to place new fields
    _inherit = 'account.invoice'
# getting field from a different model

    partner_shipping_id = fields.Many2one('res.partner', 'Shipping Address', help="Change the address only if different than in Sales Order", )
