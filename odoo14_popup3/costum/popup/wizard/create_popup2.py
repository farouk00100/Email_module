# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.exceptions import UserError

class CreatePopup2(models.TransientModel):
    _name = 'create.popup2'
    _description = 'creating a popup window that takes to what the users selected'


    destination = fields.Selection([
        ('microsoft365', 'Microsoft365'),
        ('outlook', 'Outlook'),
        ('google spread Sheet', 'Google Spread Sheet'),
    ], required=True, default='microsoft365')
    some_info = fields.Char(string="Link")

    @api.onchange("destination")
    def set_link(self):

        #get the destination value
        for rec in self:
            if (rec.destination == "microsoft365"):
                rec.some_info = "https://www.office.com/"

            if (rec.destination == "google spread Sheet"):
                print('hyaa')
                rec.some_info = "https://docs.google.com/spreadsheets/"

            if (rec.destination == "outlook"):
                rec.some_info = "https://outlook.live.com/owa/"

    def create_popup(self):

        destination = self.env.context.get('destination')
        url = ""

        if destination:
            # set the appropriate url
            if (destination == "microsoft365"):
                url = "https://www.office.com/"

            if (destination == "google spread Sheet"):
                url = "https://docs.google.com/spreadsheets/"

            if (destination == "outlook"):
                url = "https://outlook.live.com/owa/"
            return {
                'name':'go to',
                'res_model':'ir.actions.act_url',
                'type':'ir.actions.act_url',
                'url':url,
                'target':'self',
            }
        else:
            raise UserError("Unexpected error ! Contact the developer.")
