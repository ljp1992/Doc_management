# -*- coding: utf-8 -*-
from odoo import http

# class DocumentSharingSystem(http.Controller):
#     @http.route('/document_sharing_system/document_sharing_system/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/document_sharing_system/document_sharing_system/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('document_sharing_system.listing', {
#             'root': '/document_sharing_system/document_sharing_system',
#             'objects': http.request.env['document_sharing_system.document_sharing_system'].search([]),
#         })

#     @http.route('/document_sharing_system/document_sharing_system/objects/<model("document_sharing_system.document_sharing_system"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('document_sharing_system.object', {
#             'object': obj
#         })