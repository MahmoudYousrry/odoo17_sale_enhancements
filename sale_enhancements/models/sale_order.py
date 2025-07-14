from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    expected_delivery_date = fields.Datetime(string='Delivery Deadline')

    def action_confirm(self):
        res = super().action_confirm()
        for order in self:
            for picking in order.picking_ids:
                picking.date_deadline = order.expected_delivery_date

        return res