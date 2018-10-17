# coding: utf-8

import logging
from openerp import models, fields, api

_LOGGER = logging.getLogger(__name__)

class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    # Computed fields
    @api.multi
    @api.depends('property_product_pricelist')
    def _compute_fallback_pricelist(self):
        for record in self:
            record.property_product_fallback_pricelist = record.property_product_pricelist.fallback_pricelist

    property_product_fallback_pricelist = fields.Many2one('product.pricelist', compute=_compute_fallback_pricelist, readonly=True, string='Fallback Pricelist')
