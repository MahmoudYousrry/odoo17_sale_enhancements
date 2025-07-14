{
    'name': 'Sale Enhancements',
    'version': '1.0',
    'summary': 'Custom logic for Sales: Delivery Date, Category Discount, and User Commission',
    'description': """
    This module extends the Sales functionalities in Odoo by adding:
    - A custom Delivery Date field on Sale Orders
    - Category-based Discounts
    - Commission calculation for users based on their sales
    """,
    "category": "Sales",
    'author': 'Mahmoud Yousry',
    'depends': ['sale_management', 'contacts', 'stock'],
    'data': [
        'security/commission_groups.xml',
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',
        'views/product_category_views.xml',
        'views/sale_commission_views.xml',
    ],
    'installable': True,
    'application': False,
}
