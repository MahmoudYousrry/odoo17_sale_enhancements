from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange('product_id')
    def _onchange_product_discount_from_category(self):
        if self.product_id and self.product_id.categ_id:
            self.discount = self.product_id.categ_id.line_discount or 0.0
