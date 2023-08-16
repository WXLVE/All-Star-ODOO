from odoo import fields, models

# Our Tag Model
class Pear_Tag(models.Model):
    _name = "peartag.model"
    _description = "A Pear cannot and will not be a Apple ! !"
    _order = "name desc"
    #Basic
    name = fields.Char(required=True)
    color = fields.Integer("Color Index")
    
    _sql_constraints = [
        ('unique_name', 'unique (name)', 'This Tag already exists')
    ]
    # Special

