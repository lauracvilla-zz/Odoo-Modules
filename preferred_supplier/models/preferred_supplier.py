# -*- coding: utf-8 -*-

from openerp import models, fields, api, _
from openerp.tools import  float_compare
import openerp.addons.decimal_precision as dp

class product_template(models.Model):
    _inherit = 'product.template'

    preferred_supplier = fields.Many2one('res.partner', 'Preferred Supplier', readonly=True, help="You can change this field only from the Product Variant", store="true")

class product_product(models.Model):
    _inherit = 'product.product'

    from openerp.osv import fields
    def write(self, cr, uid, ids, vals, context=None):
        # print 'ovewritten write'
        # print vals
        if vals:
            if u'volume' in vals.keys():
                # print 'contains volume'
                vals['volume_holder'] = vals[u'volume']
            if u'weight' in vals.keys():
                # print 'contains weight'
                vals['weight_holder'] = vals[u'weight']

        return super(product_product, self).write(cr, uid, ids, vals, context)
        # raise Exception

    _columns = { 'preferred_supplier' : fields.many2one('res.partner', 'Preferred Supplier', help="Choose the preferred supplier to get a hint on the Purchase Order", store="true")}


    def copy_weight_volume(self, cr, uid, context=None):
        all_product_ids = self.search(cr, uid, [])
        print all_product_ids
        for product in self.browse(cr, uid, all_product_ids, context):
            print 'Copying ' + str(product.id)
            product.volume_holder = product.volume
            product.weight_holder = product.weight
