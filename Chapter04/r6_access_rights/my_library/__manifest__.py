# -*- coding: utf-8 -*-
{
    'name': "control",  # Module title
    'summary': "",  # Module subtitle phrase
    'description': """Registration and Updating of Fighters Data of the Leonardo Infante Municipality""",  # You can also rst format
    'author': "Jhonael Ramos",
    'website': "https://www.ffminfante.org.ve",
    'category': 'social',
    'version': '12.0.1',
    'depends': ['base'],
    # This data files will be loaded at the installation (commented becaues file is not added in this example)
    'data': [
        #'security/groups.xml',
        #'security/ir.model.access.csv',
        #'views/library_book.xml'
        'views/hr_employee.xml',

    ],
    # This demo data files will be loaded if db initialize with demo data (commented becaues file is not added in this example)
    # 'demo': [
    #     'demo.xml'
    # ],
}
