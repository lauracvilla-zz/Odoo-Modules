# -*- coding: utf-8 -*-
# this is responsible for creating fields in db in company model
from openerp import api, fields, models

class instagram_view_company_form(models.Model):
    #model
    _name = 'res.company'
    _inherit = 'res.company'
    #fields
    social_instagram = fields.Char("Instagram", store="True", copy="True")
    social_pinterest = fields.Char("Pinterest", store="True", copy="True")
    social_dribbble = fields.Char("Dribbble", store="True", copy="True")
