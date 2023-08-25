from odoo import models, fields

class TestModel(models.Model):
    _name = "cube.type"
    _description = "Type for cubes"

    name = fields.Char(required = True)

    
        