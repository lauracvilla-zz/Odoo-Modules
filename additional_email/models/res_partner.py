# -*- coding: utf-8 -*-

from openerp import models, fields, api, _

class ResPartnerEmail(models.Model):
    _inherit = "res.partner"

    spg_company_email = fields.Char(string='Company email', help='Shared email field among the company', widget="email", store="True")
    spg_company_email1 = fields.Char(string='Company email', help='Shared email field among the company', widget="email", store="True")

    @api.model
    def _commercial_fields(self):

        commercial_fields = super(ResPartnerEmail, self)._commercial_fields()
        new_commercial_fields = ['spg_company_email', 'spg_company_email1']
        commercial_fields.extend(new_commercial_fields)
        return commercial_fields
