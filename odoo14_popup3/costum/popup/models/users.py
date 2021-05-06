
from odoo import models, fields, api
from odoo.exceptions import UserError
import xml.etree.ElementTree as ET
import time

class PopupUsers(models.Model):
    _name = "popup.users"
    _description = "This is a table for odoo users"


    destination = fields.Selection([
        ('microsoft365', 'Microsoft365'),
        ('outlook', 'Outlook'),
        ('google spread Sheet', 'Google Spread Sheet'),
         ], required=True, default='microsoft365')

    link = fields.Char(string='Link', compute='_link_value')
    @api.depends("destination")
    def _link_value(self):
        # get the destination value
        for rec in self:
            if (rec.destination == "microsoft365"):
                rec.link = "https://www.office.com/"


            if (rec.destination == "google spread Sheet"):
                rec.link = "https://docs.google.com/spreadsheets/"

            if (rec.destination == "outlook"):
                rec.link = "https://outlook.live.com/owa/"


    def call_func(self):

        # get location value from context
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
                #print(frame.get('src'))

            # write it to xml file
            tree.write('D:\\odoo14\\costum\\popup\\views\\open_window.xml')

            # get the view_id for the popup xml file
            view_id = self.env.ref('popup.open_window_form').id

            # wait 2 second
            time.sleep(1)
            return {
                'name':'Info',
                'res_model':'open.window',
                'type':'ir.actions.act_window',
                'view_mode':'form',
                'view_type': 'form',
                'views':[(view_id,'form')],
                'view_id':'view_id',
                'res_id':'self.id',
                'target':'new',
            }
        else:
            raise UserError('Unexpected error! Contact the developer.')




