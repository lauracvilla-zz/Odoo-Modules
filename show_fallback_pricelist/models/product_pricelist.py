# coding: utf-8

import logging
from openerp import models, fields, api

_LOGGER = logging.getLogger(__name__)

class ProductPricelist(models.Model):
    _name = 'product.pricelist'
    _inherit = 'product.pricelist'

    # Computed fields
    @api.multi
    @api.depends('item_ids')
    def _compute_fallback_pricelist(self):
        for record in self:
            for item in record.item_ids:
                if item.applied_on == '3_global':
                    record.fallback_pricelist = item.base_pricelist_id

    fallback_pricelist = fields.Many2one('product.pricelist', compute=_compute_fallback_pricelist, readonly=True)
