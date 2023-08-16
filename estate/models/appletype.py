from odoo import fields, models


class Apple_Type(models.Model):
    _name = "appletype.model"
    _description = "A Pear is not a Apple"
    _order = "sequence, name"
    _sql_constraints = [
        ('unique_name', 'unique (name)', 'This Type already exists')
    ]
    #Basic
    name = fields.Char( required=True)
    description = fields.Text()
    sequence = fields.Integer('Sequence', default=10, help="Used to order stages. Lower is better.")
    # Relational (for inline view)
    property_ids = fields.One2many("apple.model", "apple_type_id", string = "Apples")

    # Special
    offer_count = fields.Integer(string="Offers Count", compute="_compute_offer")
    offer_ids = fields.Many2many("appleoffer.model", string="Offers", compute="_compute_offer")

    def _compute_offer(self):
        # This solution is quite complex. It is likely that the trainee would have done a search in
        # a loop.
        data = self.env["appleoffer.model"].read_group(
            [("property_id.state", "!=", "canceled"), ("apple_type_id", "!=", False)],
            ["ids:array_agg(id)", "apple_type_id"],
            ["apple_type_id"],
        )
        mapped_count = {d["apple_type_id"][0]: d["apple_type_id_count"] for d in data}
        mapped_ids = {d["apple_type_id"][0]: d["ids"] for d in data}
        for prop_type in self:
            prop_type.offer_count = mapped_count.get(prop_type.id, 0)
            prop_type.offer_ids = mapped_ids.get(prop_type.id, [])

    # ---------------------------------------- Action Methods -------------------------------------

    def action_view_offers(self):
        res = self.env.ref("estate.apple_offer_action").read()[0]
        res["domain"] = [("id", "in", self.offer_ids.ids)]
        return res