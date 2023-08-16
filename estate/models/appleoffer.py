from odoo import api, fields, models
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError
from odoo.tools import float_compare
# from openerp import api

class Apple_Offer(models.Model):
    _name = "appleoffer.model"
    _description = "A Apple is never free, there are always worms!"
    _order = "price desc"
    _sql_constraints = [
        ('check_price', 'CHECK(price > 0)',
         'The amount of an expected price should be higher then 0!')
    ]
    
    #Basic
    name = fields.Char(default = "Offer")
    price = fields.Float()
    validity = fields.Integer(string="Validity (days)", default=7)
    #Special
    status = fields.Selection(
            selection=[
                ("accepted", "Accepted"),
                ("refused", "Refused"),
            ],       
            string="Status",
            required=False,
            copy=False,
            default=False,

        )
    
    #IDs and Relational
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    property_id = fields.Many2one('apple.model', string="Apples", required=True)

    # For stat button:
    apple_type_id = fields.Many2one(
        "appletype.model", related="property_id.apple_type_id", string="Apple Type", store=True
    )

    #Computed
    date_deadline = fields.Date(string="Deadline", compute="_compute_date_deadline", inverse="_inverse_date_deadline")
    
    

    @api.depends('create_date')
    def _inverse_email_from(self):
        for lead in self:
                if lead.date_deadline != lead.create_date + lead.validity:
                    lead.date_deadline == lead.create_date + lead.validity
                    
                    
    @api.depends("create_date", "validity")
    def _compute_date_deadline(self):
        for offer in self:
            date = offer.create_date.date() if offer.create_date else fields.Date.today()
            offer.date_deadline = date + relativedelta(days=offer.validity)

    def _inverse_date_deadline(self):
        for offer in self:
            date = offer.create_date.date() if offer.create_date else fields.Date.today()
            offer.validity = (offer.date_deadline - date).days

    # ------------------------------------------ CRUD Methods -------------------------------------

    @api.model
    def create(self, vals):
        if vals.get("property_id") and vals.get("price"):
            prop = self.env["apple.model"].browse(vals["property_id"])
            # We check if the offer is higher than the existing offers
            if prop.offer_ids:
                max_offer = max(prop.mapped("offer_ids.price"))
                if float_compare(vals["price"], max_offer, precision_rounding=0.01) <= 0:
                    raise UserError("The offer must be higher than %.2f" % max_offer)
            prop.state = "offer_received"
        return super().create(vals)

    # ---------------------------------------- Action Methods -------------------------------------

    def action_accept(self):
        if "accepted" in self.mapped("property_id.offer_ids.state"):
            raise UserError("An offer as already been accepted.")
        self.write(
            {
                "state": "accepted",
            }
        )
        return self.mapped("property_id").write(
            {
                "state": "offer_accepted",
                "selling_price": self.price,
                "buyer_id": self.partner_id.id,
            }
        )

    def action_refuse(self):
        return self.write(
            {
                "state": "refused",
            }
        )