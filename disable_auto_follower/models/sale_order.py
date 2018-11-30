# coding: utf-8

import logging
from openerp import models, fields

_LOGGER = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _name = 'sale.order'
    _inherit = 'sale.order'

    has_removed_auto_followers = fields.Boolean('Has removed Auto Followers')
