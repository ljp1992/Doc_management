# -*- coding: utf-8 -*-

from odoo import models, fields, api

class DocumentSharingSystem(models.Model):
    _name = 'document.sharing.system'

    name = fields.Char(string=u'标题')
    content = fields.Text(string=u'内容')

    # category_ids = fields.Many2many('doc.category', 'doc_cateory_rel', 'doc_id', 'category_id', string=u'类别')

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        # print self.env.context
        # print args,offset,limit,order,count
        if self.env.context.get('search_field') == 'name':
            val = ''
            for item in args:
                if item[0] == 'name':
                    val = item[2]
            if val:
                args = ['|', ('content', 'ilike', val)] + args
        return super(DocumentSharingSystem, self).search(args, offset, limit, order, count=count)