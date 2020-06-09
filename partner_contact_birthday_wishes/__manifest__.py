{
    'name': "Contacts Birthday Wishes",
    'summary': 'Envía emails con felicitaciones de cumpleaños a los contactos.',
    'author': 'Inma Sánchez',
    'website': 'https://github.com/EDallas89/partner_contact',
    'license': 'AGPL-3',
    'category': "Extra Tools",
    'version': "12.0.1.0",
    'data': [
        'views/partner_birthday_wishes_cron.xml',
        'data/partner_birthday_wishes_email.xml'
    ],
    'depends': [
        'contacts',
        'partner_contact_birthdate',
        'partner_contact_personal_information_page'
    ],
    'installable': True,
}
