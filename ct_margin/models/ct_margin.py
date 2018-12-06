# -*- coding: utf-8 -*-

from openerp import api, models, fields

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    ct_margin = fields.Char(compute='_get_ct_margin', string='Margin')

    @api.one
    @api.depends('discount','purchase_price','product_uom_qty','price_unit')
    def _get_ct_margin(self):
        #set values to 0 for calculation
        s_price=0
        discount=0
        cost=0
        margin=0
        margin_percentage=0
        for record in self:
            if record.product_id:
                # calculations - you can reuse it in other modules
                s_price = record.price_unit * record.product_uom_qty
                discount = (s_price*record.discount)/100
                cost = record.purchase_price * record.product_uom_qty
                margin = (s_price - discount) - cost
                # add record.another field to set results for other fields u want
                record.ct_margin = str(round(margin,2))
