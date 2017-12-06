# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Diary(models.Model):
    _name = 'diary'

    name = fields.Char(string=u'标题')
    date = fields.Date(default=lambda self: self._context.get('date', fields.Date.context_today(self)),
                       string=u'日期')
    content = fields.Text(string=u'内容')
