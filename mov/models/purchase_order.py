# -*- coding: utf-8 -*-

from openerp import models, fields, api

class pucrhase_order(models.Model):
    _inherit = 'purchase.order'

    mov_child = fields.Char(string='MOV', help='Minimum Order Value', related="partner_id.mov", readonly="True")
    mov_parent = fields.Char(string='MOV', help='Minimum Order Value', related="partner_id.parent_id.mov", readonly="True")
