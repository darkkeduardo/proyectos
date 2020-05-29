# -*- coding: utf-8 -*-
# from odoo import http


# class Proyecto(http.Controller):
#     @http.route('/proyecto/proyecto/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/proyecto/proyecto/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('proyecto.listing', {
#             'root': '/proyecto/proyecto',
#             'objects': http.request.env['proyecto.proyecto'].search([]),
#         })

#     @http.route('/proyecto/proyecto/objects/<model("proyecto.proyecto"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('proyecto.object', {
#             'object': obj
#         })
