
from odoo import fields, models, api
from odoo.exceptions import ValidationError, UserError
from odoo.tools import float_compare, float_is_zero
from dateutil.relativedelta import relativedelta
# from openerp import api

    
class simple_Apple(models.Model):
    #Naming Our Model
    _name = "apple.model"
    _description = "Apple makes Apples"
    _order = "id desc"
    
    _sql_constraints = [
        ("check_expected_price", "CHECK(expected_price > 0)", "The expected price must be strictly positive"),
        ("check_selling_price", "CHECK(selling_price >= 0)", "The offer price must be positive"),
    ]
    
    def _default_date_availability(self):
        return fields.Date.context_today(self) + relativedelta(months=3)
    
    #Basic
    name = fields.Char( required=True)
    description = fields.Text("Description")
    postcode = fields.Char("Postcode")
    date_availability = fields.Date("Available From", default=lambda self: self._default_date_availability(), copy=False)
    expected_price = fields.Float("Expected Price", required=True)
    selling_price = fields.Float("Selling Price", copy=False, readonly=True)
    bedrooms = fields.Integer("Bedrooms", default=2)
    living_area = fields.Integer("Living Area (sqm)")
    facades = fields.Integer("Facades")
    garden = fields.Boolean("Garden")
    garden_area = fields.Integer("Garden Area (sqm)")
    orientation = fields.Selection(
        selection=[
            ("north", "North"),
            ("east", "East"),
            ("west", "West"),
            ("south", "South"),
            ("canceled", "Canceled"),
            ],
            string="Orientation",
            copy=False,
        )
    
    # Special and IDS
    apple_type_id = fields.Many2one('appletype.model', string='Apple Types')
    salesman_id = fields.Many2one("res.users", string="Salesman", default=lambda self: self.env.user)
    buyer_id = fields.Many2one("res.partner", string="Buyer", readonly=True, copy=False)
    tag_ids = fields.Many2many('appletag.model', string="Tags")
    offer_ids = fields.One2many('appleoffer.model',"property_id", string = "Offers")
    
    

    # computed
    total_area = fields.Integer(
        "Total Area (sqm)",
        compute="_compute_total",
        help="Total area computed by summing the living area and the garden area",
    )
    best_offer = fields.Char("Best Offer", compute="_compute_best_offer", help="Best offer received")

    #Active or Not?
    active = fields.Boolean("Active", default=True)
    
    # Selection
    state = fields.Selection(
        selection=[
            ("new", "New"),
            ("offer_received", "Offer Received"),
            ("offer_accepted", "Accepted"),
            ("sold", "Sold"),
            ("canceled", "Canceled"),
        ],
        string="Status",
        required=True,
        copy=False,
        default="new",
    )

    # ------------------------------------------ CRUD Methods -------------------------------------

    def unlink(self):
        if not set(self.mapped("state")) <= {"new", "canceled"}:
            raise UserError("Only new and canceled properties can be deleted.")
        return super().unlink()

    # ---------------------------------------- Compute methods ------------------------------------

    @api.depends("living_area", "garden_area")
    def _compute_total(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area
            
    @api.depends('offer_ids.price')
    def _compute_best_offer(self):
        for record in self:
            record.best_offer = max(record.offer_ids.mapped("price")) if record.offer_ids else 0.0


    # ----------------------------------- Constrains and Onchanges --------------------------------

            
    @api.onchange("garden")
    def _onchange_partner_id(self):
        if self.garden:
            self.garden_area = 10
            self.orientation = "north"
        else: 
            self.garden_area = 0
            self.orientation = False
        
    @api.constrains("expected_price", "selling_price")
    def _check_price_difference(self):
        for prop in self:
            if (
                not float_is_zero(prop.selling_price, precision_rounding=0.01)
                and float_compare(prop.selling_price, prop.expected_price * 90.0 / 100.0, precision_rounding=0.01) < 0
            ):
                raise ValidationError(
                    "The selling price must be at least 90% of the expected price! "
                    + "You must reduce the expected price if you want to accept this offer."
                )
        
    # ---------------------------------------- Action Methods -------------------------------------  
        
        
    def action_sold(self):
        if "canceled" in self.mapped("state"):
            raise UserError("Canceled properties cannot be sold.")
        return self.write({"state": "sold"})

    def action_cancel(self):
        if "sold" in self.mapped("state"):
            raise UserError("Sold properties cannot be canceled.")
        return self.write({"state": "canceled"})
    

    # def action_do_accept(self):
    #     for record in self:
    #             if record.buyer_id == "" and record.selling_price != "":
    #                 record.status = "accepted"
    #                 latest_offer = self.env[record.offer_ids].search([], limit=1, order='create_date desc')
    #                 latest_offer.status = "accepted"
    #                 record.buyer_id = latest_offer.partner_id
    #                 record.selling_price = latest_offer.price
    #     return True
    
    # def action_do_refuse(self):
    #     for record in self:
    #         if record.buyer_id != "" and record.selling_price != "":
    #             record.status = "accepted"
    #             latest_offer = self.env[record.offer_ids].search([], limit=1, order='create_date desc')
    #             latest_offer.status = "refused"
    #     return True
    
