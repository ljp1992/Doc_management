# -*- coding: utf-8 -*-

from odoo import models, fields, api

class document_sharing_system(models.Model):
    _name = 'document.sharing.system'

    name = fields.Char(string=u'标题')
    content = fields.Text(string=u'内容')

    category_ids = fields.Many2many('doc.category', 'doc_cateory_rel', 'doc_id', 'category_id', string=u'类别')
