# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SecretIdentity(models.Model):
    _name = 'superhero.secret.identity'
    _description = 'Superhero Secret identities'
    _rec_name = 'first_name'

    first_name = fields.Char(required=True)
    last_name = fields.Char()
    date_of_birth = fields.Date()

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
