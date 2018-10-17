# -*- coding: utf-8 -*-

from openerp import api, fields, models, _

class Bukcirra(models.Model):
# where to place new fields
    _inherit = 'stock.picking'
# getting user_id to the stock picking
    user_id = fields.Many2one('res.users', string='Salesperson', track_visibility='onchange',
        readonly=True, states={'draft': [('readonly', False)]},
        default=lambda self: self.env.user)
