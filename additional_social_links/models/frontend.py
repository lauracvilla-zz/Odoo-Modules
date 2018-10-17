# -*- coding: utf-8 -*-
# this is responsible for creating fields in db in website model
from openerp import api, fields, models

class instagram_website(models.Model):
#model
    _name = 'website'
    _inherit = "website"
    # fields
    social_instagram = fields.Char("Instagram", store="True", copy="True", related="company_id.social_instagram" )
    social_pinterest = fields.Char("Pinterest", store="True", copy="True", related="company_id.social_pinterest" )
    social_dribbble = fields.Char("Dribbble", store="True", copy="True", related="company_id.social_dribbble" )
