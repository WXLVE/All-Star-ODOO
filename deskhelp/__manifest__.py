# -*- coding: utf-8 -*-

{
    'name': 'Questions',
    'description': "Where Questions get answers" , 
    'depends': [
        'base',
        'web',
    ],
    
    
  'data': [
        
        #security
        # 'security/crm_security.xml',
        'security/ir.model.access.csv',


        #views
        'views/helpdesk_question_views.xml',
        
        'views/documentation_tags.xml',
        'views/documentation.xml',
        'views/helpdesk_menus.xml',



    ],
    "application": True,
}