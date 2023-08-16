from odoo import fields, models


class Documentation_Tag(models.Model):
    _name = "documentationtag.model"
    _description = "You can TAG a Documentation"
    _order = "name desc"
    #Basic
    name = fields.Char(required=True)
    color = fields.Integer("Color Index")
    
    _sql_constraints = [
        ('unique_name', 'unique (name)', 'This Tag already exists')
    ]
    # Special
