from datetime import datetime
from odoo import SUPERUSER_ID
from odoo import api, models


class res_partner(models.Model):
    _inherit = "res.partner"

    @api.model
    def mail_reminder(self):
        today = datetime.now().date()
        for partner in self.search([]):
            if partner.birthdate_date:
                birthdate = datetime.strptime(
                    str(partner.birthdate_date), '%Y-%m-%d').date()
                if (
                    today.day == birthdate.day and
                    today.month == birthdate.month and
                        today.year != birthdate.year):
                    self.send_birthday_wishes(partner.id)
        return

    @api.model
    def send_birthday_wishes(self, partner_id):
        su_id = self.env['res.partner'].browse(SUPERUSER_ID)
        template_id = self.env['ir.model.data'].get_object_reference(
            'partner_contact_birthday_wishes',
            'partner_contact_birthday_wishes_email_template')[1]
        email_template = self.env['mail.template'].browse(template_id)
        email_to = self.env['res.partner'].browse(partner_id).email
        if template_id:
            values = email_template.generate_email(partner_id, fields=None)
            values['email_to'] = email_to
            values['email_from'] = su_id.email
            values['res_id'] = False
            mail_mail_obj = self.env['mail.mail']
            mail_mail_obj.create(values)
        return True
