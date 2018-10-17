# -*- coding: utf-8 -*-

from openerp import api, fields, models, _

class Shipping_Invoice(models.Model):
# where to place new fields
    _inherit = 'account.invoice'
# getting user_id to the stock picking

    partner_shipping_id = fields.Many2one('res.partner', string='Partner',
        store=True, readonly=True, related_sudo=False)

    address_shipping_idss = fields.Many2one(
            'res.partner',
            'Shipping Address',
            readonly=True)
