from odoo import fields, models


class ResUsers(models.Model):

    # ---------------------------------------- Private Attributes ---------------------------------
    _inherit = "res.users"

    # --------------------------------------- Fields Declaration ----------------------------------

    # Relational
    # This domain gives the opportunity to mention the evaluated and non-evaluated domains
    property_ids = fields.One2many(
        "cube.model", "salesman_id", string="Properties",
    )