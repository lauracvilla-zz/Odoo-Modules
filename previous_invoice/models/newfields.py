from openerp import models, fields

class OldInvoiceNo(models.Model):
# where to place new fields

    _inherit = 'account.invoice'
# getting the vat field to accounting model
    old_invoice = fields.Char(string='Previous Invoice No')
