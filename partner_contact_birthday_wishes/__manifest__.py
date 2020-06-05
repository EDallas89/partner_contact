{
    'name': "Contacts Birthday Wishes",
    'summary': 'Send Birthday Greetings Email to Contacts',
    'author': 'Inma Sánchez, '
              'Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/partner-contact',
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
