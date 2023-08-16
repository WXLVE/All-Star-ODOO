
from odoo import fields, models, api
from odoo.exceptions import ValidationError, UserError
from odoo.tools import float_compare, float_is_zero
from dateutil.relativedelta import relativedelta
# from openerp import api

    
class simple_Question(models.Model):
    #Naming Our Model
    _name = "question.model"
    _description = "A man wonders, A Question answers"
    _order = "id desc"
    #FIELDS
        
    #Basic
    name = fields.Char("Question", required=True)
    description = fields.Html("Description", required=True)
    
