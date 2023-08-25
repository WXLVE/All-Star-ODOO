from odoo import models, fields

class Typemodel(models.Model):
    _name = "cube.type"
    _description = "Type for cubes"

    name = fields.Char(required = True)

    
        