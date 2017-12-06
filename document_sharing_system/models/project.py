# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Project(models.Model):
    _name = 'project'

    name = fields.Char(string=u'项目名称')
    start_date = fields.Date(default=lambda self: self._context.get('date', fields.Date.context_today(self)),
                             string=u'开始日期')
    stop_date = fields.Date(default=lambda self: self._context.get('date', fields.Date.context_today(self)),
                            string=u'结束日期')
    description = fields.Text(string=u'描述')

    requirement_ids = fields.One2many('requirement', 'project_id')

    def write(self, vals):
        if vals.get('requirement_ids'):
            sort_requirement_ids = []
            for item in vals.get('requirement_ids'):
                if item[0] == 2:
                    sort_requirement_ids.insert(0, item)
                else:
                    sort_requirement_ids.append(item)
            vals['requirement_ids'] = sort_requirement_ids
        print vals
        return super(Project, self).write(vals)

class Project(models.Model):
    _inherit = 'project'

    start_date = fields.Date(default=lambda self: self._context.get('date', fields.Date.context_today(self)),
                             string=u'start date')