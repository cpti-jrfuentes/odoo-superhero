# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SuperPower(models.Model):
    _name = 'superhero.super.power'
    _description = 'Superhero Super Power'
    _rec_name = 'name'

    name = fields.Char(required=True)
    description = fields.Char(required=True)
    superhero_ids = fields.Many2many("superhero.superhero",string="Superheroes")

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
