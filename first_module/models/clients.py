# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError


class EmailClients(models.Model):
    _name = "first_module.clients"
    _description = "Email Client"

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string="Email", size=30, required=True)
    email_provider = fields.Selection([
        ('Gmail', 'https://www.gmail.com'),
        ('office 365', 'https://www.office.com'),
        ('icloud', 'iCloud'),
    ], required=True, default='Office 365')
