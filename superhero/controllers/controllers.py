# -*- coding: utf-8 -*-
# from odoo import http


# class Superhero(http.Controller):
#     @http.route('/superhero/superhero', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/superhero/superhero/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('superhero.listing', {
#             'root': '/superhero/superhero',
#             'objects': http.request.env['superhero.superhero'].search([]),
#         })

#     @http.route('/superhero/superhero/objects/<model("superhero.superhero"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('superhero.object', {
#             'object': obj
#         })
