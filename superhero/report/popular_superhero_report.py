# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import UserError


class PopularSuperheroReport(models.TransientModel):
#    _name = 'report.superhero.report_popular_superheroes'

    @api.model
    def _get_report_values_backup(self, docids, data=None):
        raise UserError("SHOULD NOT 1")
        report_name = 'superhero.report_popular_superheroes'
        report = self.env['ir.actions.report']._get_report_from_name(report_name)
        return {
            'doc_ids': {2},
            'doc_model': report.model,
            'docs': self.env[report.model].search([]),
        }

    @api.model
    def _get_report_values(self, docids, data=None):
        raise UserError("SHOULD NOT 2")
        records = self.env['superhero.superhero'].search([])
        docs = []
 
        for hero in records:
            docs.append({
                'name': hero.name,
            })

        return {
            'docs': records
        }
