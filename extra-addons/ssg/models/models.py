# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class ssg(models.Model):
#     _name = 'ssg.ssg'
#     _description = 'ssg.ssg'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


from odoo import models, fields, api

class SsgSsg(models.Model):
    _name = 'ssg.ssg'
    _description = 'ssg.ssg'
    name = fields.Integer(string="Número incidencia")
    fecha = fields.Date(string="Fecha")
    description = fields.Char(string="Usuario que atiende la incidencia.")
