from odoo import models, fields
from dateutil.relativedelta import relativedelta

class TestModel(models.Model):
    _name = "cube.model"
    _description = "Model for cubes"

    def _default_date_availability(self):
        return fields.Date.context_today(self) + relativedelta(months=3)

    name = fields.Char(required = True)
    description = fields.Char('Description')
    postcode = fields.Char('Postcode')
    date_availability = fields.Date('Date Availability', default=lambda self: self._default_date_availability(), copy=False)
    expected_price = fields.Float('Expected Price', required=True)
    selling_price = fields.Float('Selling Price', readonly=True, copy=False)
    bedrooms = fields.Integer('Bedrooms', default=2)
    living_area = fields.Integer('Living Area')
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden')
    garden_area = fields.Integer('Garden Area')
    active = fields.Boolean("Active", default=True)
    orientation = fields.Selection(
        selection = [
            ("north", "North"),
            ("east", "East"),
            ("west", "West"),
            ("south", "South"),
            ("canceled", "Canceled"),
            ],
            string = "Orientation",
            copy = False,
        )
    
    # Special and IDS
    cube_type_id = fields.Many2one('cube.type', string='Cube Types')
    salesman_id = fields.Many2one("res.users", string="Salesman", default=lambda self: self.env.user)
    buyer_id = fields.Many2one("res.partner", string="Buyer", readonly=True, copy=False)

    state = fields.Selection(
        selection = [
            ("new", "New"),
            ("offer_received", "Offer Received"),
            ("offer_accepted", "Offer Accepted"),
            ("sold", "Sold"),
            ("canceled", "Canceled"),
            ],
            string = "State",
            required = True,
            copy = False,
            default = "new",
        )

