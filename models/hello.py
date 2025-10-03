# -*- coding: utf-8 -*-
from odoo import models, fields, api

class HelloWorld(models.Model):
    _name = "hello.world"
    _description = "Hello World"

    name = fields.Char(string="Title", required=True)
    note = fields.Text(string="Note")
    active = fields.Boolean(string="Active", default=True)

    @api.model
    def create(self, vals):
        # small demonstration hook
        record = super().create(vals)
        # you could add logging or additional actions here
        return record
