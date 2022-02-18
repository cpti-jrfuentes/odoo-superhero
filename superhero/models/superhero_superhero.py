# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Superhero(models.Model):
    _name = 'superhero.superhero'
    _description = 'Superhero Superhero'
    _rec_name = 'name'

    name = fields.Char(required=True)
    super_power_ids = fields.Many2many("superhero.super.power",string="Super Powers")
    secret_identity_id = fields.Many2one("superhero.secret.identity",string="Secret Identity",required=True)
    country_id = fields.Many2one("res.country",string="Country")
    fans = fields.Integer(required=True)

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
