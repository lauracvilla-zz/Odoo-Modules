# -*- coding: utf-8 -*-
# (C) Piotr Cierkosz - See the license for more details
# Module was produced in a good faith, it was tested with clean Odoo 11 version and no errors were detectedself.
# Can't guarantee proper work of the module and I don't take responsibility for errors caused by itself.
# E-mail me with any questions.
{
    'name': 'Instagram, Pinterest and Dribbble on Website and Blog',
    'author': 'Piotr Cierkosz',
    'website': 'http://www.cier.tech',
    'version': '1.0',
    'category': 'Website',
    'images': ['images/thumbnail.png'],
    'depends' : ['website', 'website_blog'],
    'installable' : True,
    'license': 'Other proprietary',
    'summary': 'Adds Instagram, Pinterest and Dribbble to the website footer and blog',
    'price': 9.0,
    'currency': 'EUR',
    'auto_install': False,
    'data': [
        'views/website_footer_new_social.xml',
        'views/company_form_new_social.xml',
        'views/blog_new_social.xml',
    # Please uncomment the field below if you are using Email Marketing module
    #   'views/company_form_mass_mailing.xml',
    ],
    'description': """
    Adds Instagram, Pinterest and Dribble to Website footer as well as in the company.
    """
}