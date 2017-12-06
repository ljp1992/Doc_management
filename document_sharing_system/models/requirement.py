# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Requirement(models.Model):
    _name = 'requirement'

    name = fields.Char(string=u'需求名称')
    description = fields.Text(string=u'描述')

    project_id = fields.Many2one('project', string=u'项目')

    start_date = fields.Date(default=lambda self: self._context.get('date', fields.Date.context_today(self)),
                             string=u'开始日期')
    stop_date = fields.Date(default=lambda self: self._context.get('date', fields.Date.context_today(self)),
                            string=u'结束日期')

    price_unit = fields.Float(string=u'不含税单价')
    qty = fields.Float(string=u'数量')
    tax_amount = fields.Float(string=u'税率')
    price_total = fields.Float(string=u'含税合计', compute='_compute_amount', store=True)
    price_subtotal = fields.Float(string=u'不含税合计', compute='_compute_amount', store=True)

    state = fields.Selection(selection=[('draft',u'待处理'),
                                        ('develop',u'开发中'),
                                        ('check',u'测试中'),
                                        ('done',u'完成'),
                                        ('cancel',u'取消')], default='draft', string=u'状态')

    @api.model
    def create(self, vals):
        print 'Requirement create'
        return super(Requirement, self).create(vals)

    @api.multi
    def write(self, vals):
        print 'Requirement write'
        return super(Requirement, self).write(vals)

    @api.multi
    def unlink(self):
        print 'Requirement unlink'
        return super(Requirement, self).unlink()

    @api.multi
    @api.depends('price_unit', 'qty', 'tax_amount')
    def _compute_amount(self):
        print '_compute_amount',self
        for record in self:
            print 'record:',record,record.id
            # print 11111111
            # print record.price_unit
            # print 22222222
            # print record,record.price_unit,record.qty,record.tax_amount
            price_total = record.price_unit * (1 + record.tax_amount * 0.01) * record.qty
            price_subtotal = record.price_unit * record.qty
            print {'price_total':price_total,
                   'price_subtotal':price_subtotal,}
            record.update({'price_total':price_total,
                           'price_subtotal':price_subtotal,})