from odoo import fields, models

class ProductCategory(models.Model):
    _inherit = 'product.category'

    line_discount = fields.Float(string="Discount (%)")
