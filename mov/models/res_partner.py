# -*- coding: utf-8 -*-

from openerp import models, fields, api, _

class ResPartnerMov(models.Model):
    _inherit = "res.partner"

    mov = fields.Char(string='MOV', help='Minimum Order Value')
    mov1 = fields.Char(string='MOV', help='Minimum Order Value')

    @api.model
    def _commercial_fields(self):
        """ Returns the list of fields that are managed by the commercial entity
        to which a partner belongs. These fields are meant to be hidden on
        partners that aren't `commercial entities` themselves, and will be
        delegated to the parent `commercial entity`. The list is meant to be
        extended by inheriting classes. """
        commercial_fields = super(ResPartnerMov, self)._commercial_fields()
        new_commercial_fields = ['mov', 'mov1']
        commercial_fields.extend(new_commercial_fields)
        return commercial_fields
