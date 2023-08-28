from odoo import fields, models

class Cube_Tag(models.Model):
    _name = "cubetag.model"
    _description = "A Cube Is Something Else Than A Rectangle"
    _order = "name desc"
    #Basic
    name = fields.Char(required=True)
    # color = fields.Integer("Color Index")
    
    _sql_constraints = [
        ('unique_name', 'unique (name)', 'This Tag already exists')
    ]
    # Special