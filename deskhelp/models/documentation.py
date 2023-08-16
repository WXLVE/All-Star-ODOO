
from odoo import fields, models, api
from odoo.exceptions import ValidationError, UserError
from odoo.tools import float_compare, float_is_zero
from dateutil.relativedelta import relativedelta
# from openerp import api

    
class simple_documentation(models.Model):
    #Naming Our Model
    _name = "documentation.model"
    _description = "Answers answer Questions"
    _order = "id desc"
    
    #Basic
    name = fields.Char( required=True)
    description = fields.Html("Description")
    
    # Special and IDS
    tag_ids = fields.Many2many('documentationtag.model', string="Tags")


