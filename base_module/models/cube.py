from odoo import models, fields

class TestModel(models.Model):
    _name = "cube.model"
    _description = "Model for cubes"

    name = fields.Char(required = True)
    expected_price = fields.Float("Expected Price", required=True)