# -*- coding: utf-8 -*-

from odoo import models, fields, api

class DocCategory(models.Model):
    _name = 'doc.category'

    name = fields.Char(string=u'名称')

    # doc_ids = fields.Many2many('document.sharing.system', 'doc_cateory_rel', 'category_id', 'doc_id', string=u'文档')
