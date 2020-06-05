# -*- coding: utf-8 -*-
{
    'name': "Contacts Birthday on Calendar",
    'summary': """
        Añade los cumpleaños de los contactos al calendario""",
    'author': "Inma Sánchez y Carlos Ramos",
    'website': "https://github.com/EDallas89",
    'category': 'Extra Tools',
    'version': '12.0.1.0.0',
    'depends': [
        'calendar',
        'contacts',
        'partner_contact_birthdate',
    ],
    'data': [
        'data/partner_contact_birthday_calendar_data.xml',
        'views/partner_contact_birthday_calendar_cron.xml',
        'views/res_partner.xml',
    ],
    'installable': True,
    'application': True,
}
