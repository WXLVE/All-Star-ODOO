# from odoo import api, fields, models
# from dateutil.relativedelta import relativedelta
# from odoo.exceptions import UserError
# from odoo.tools import float_compare

# class Cube_Offer(models.Model):
#     _name = "cubeoffer.model"
#     _description = "These are offers for Rubiks cubes"
#     _order = "price desc"

#     _sql_constraints = [
#         ('check_price', 'CHECK(price > 0)',
#          'The amount of an expected price should be higher then 0!')
#     ]

#     price = fields.Float()

#     status = fields.Selection(
#             selection=[
#                 ("accepted", "Accepted"),
#                 ("refused", "Refused"),
#             ],       
#             string="Status",
#             required=False,
#             copy=False,
#             default=False,

#         )
    
#     partner_id = fields.Many2one("res.partner", string="Partner", required=True)
#     property_id = fields.Many2one('cube.model', string="Cubes", required=True)