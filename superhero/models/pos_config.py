# -*- coding: utf-8 -*-

from odoo import api, fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    superhero_id = fields.Many2one('superhero.superhero', string="Superhero")

#    def set_values(self):
#        super(ResConfigSettings, self).set_values()
#        if not self.group_product_pricelist:
#            configs = self.env['pos.config'].search([('use_pricelist', '=', True)])
#            for config in configs:
#                config.use_pricelist = False
