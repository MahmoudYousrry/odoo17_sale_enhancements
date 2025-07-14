from odoo import models, fields, api

class SaleCommission(models.Model):
    _name = 'sale.commission'
    _description = 'Sales Commission'

    user_id = fields.Many2one('res.users', string='Salesperson', required=True)

    min_target = fields.Float(string='Min Target')
    max_target = fields.Float(string='Max Target')
    below_min_percentage = fields.Float(string="Below Min %")
    between_min_max_percentage = fields.Float(string="Between Min/Max %")
    above_max_percentage = fields.Float(string="Above Max %")

    currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
        default=lambda self: self.env.company.currency_id,
        required=True
    )

    achieved_amount = fields.Monetary(
        string='Achieved Amount',
        compute='_compute_achieved_amount',
        store=True,
        currency_field='currency_id'
    )

    commission_percentage = fields.Float(
        string='Commission %',
        compute='_compute_commission',
        store=True
    )

    commission_amount = fields.Monetary(
        string='Commission Amount',
        compute='_compute_commission',
        store=True,
        currency_field='currency_id'
    )

    @api.depends('user_id')
    def _compute_achieved_amount(self):
        for rec in self:
            orders = self.env['sale.order'].search([
                ('user_id', '=', rec.user_id.id),
                ('state', '=', 'sale')
            ])
            rec.achieved_amount = sum(orders.mapped('amount_total'))

    @api.depends('min_target', 'max_target', 'achieved_amount',
                 'below_min_percentage', 'between_min_max_percentage', 'above_max_percentage')
    def _compute_commission(self):
        for rec in self:
            if rec.achieved_amount < rec.min_target:
                rec.commission_percentage = rec.below_min_percentage or 0.0
            elif rec.min_target <= rec.achieved_amount <= rec.max_target:
                rec.commission_percentage = rec.between_min_max_percentage or 0.0
            elif rec.achieved_amount > rec.max_target:
                rec.commission_percentage = rec.above_max_percentage or 0.0
            else:
                rec.commission_percentage = 0.0

            rec.commission_amount = rec.achieved_amount * (rec.commission_percentage / 100)
