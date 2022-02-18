# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import UserError


class PopularSuperheroWizard(models.TransientModel):
    _name = 'popular.superhero.wizard'
    _description = 'Popular Superhero Wizard'

    fans = fields.Integer()

    @api.model
    def action_print_report(self, data):
        records = self.env['superhero.superhero'].search([])
        recs = []
 
        for hero in records:
            recs.append({
                'name': hero.name,
                'identity': hero.secret_identity_id.first_name,
                'fans': hero.fans
            })
        recs.sort(key=lambda r: r['fans'], reverse=True)
        data = {
            'recs': recs
        }
        # raise UserError(data)
        return self.env.ref('superhero.action_popular_superheroes_report').report_action(self, data=data)

