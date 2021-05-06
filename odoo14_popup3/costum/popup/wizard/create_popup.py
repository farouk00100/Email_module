# -*- coding: utf-8 -*-

from odoo import fields, models, api
import xml.etree.ElementTree as ET
from odoo.exceptions import UserError
import time


class CreatePopup(models.TransientModel):
    _name = 'create.popup'
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
                url = "https://docs.google.com/spreadsheets/u/0/"

            if (destination == "outlook"):
                url = "https://outlook.live.com/owa/"

            # parse the xml file and get the root
            tree = ET.parse('D:\\odoo14\\costum\\popup\\views\\open_window.xml')
            root = tree.getroot()

            # search for the frame tag and change the src value
            for frame in root.iter('iframe'):
                frame.set("src", url)

            # write it to xml file
            tree.write('D:\\odoo14\\costum\\popup\\views\\open_window.xml')

            # get the view_id for the popup xml file
            view_id = self.env.ref('popup.open_window_form').id

            # wait 1 second
            time.sleep(1)
            return {
                'name': 'Info',
                'res_model': 'open.window',
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'view_type': 'form',
                'views': [(view_id, 'form')],
                'view_id': 'view_id',
                'res_id': 'self.id',
                'target': 'new',
            }

        else:
            raise UserError("Unexpected error ! Contact the developer.")
