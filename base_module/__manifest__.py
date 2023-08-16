# -*- coding: utf-8 -*-
# Here we Initialize the Model, Dependencies, Files and Views we want to Include
{
    'name': 'Pears',
    'description': "This a Example Module" , 
    'depends': [
        'base',
        'web',
        'web_map',
    ],
    
    
  'data': [
        
        # security

        'security/ir.model.access.csv',


        # views
        'views/pear_offers.xml',
        'views/pear_tags.xml',
        'views/pear_types.xml',
        'views/pear_views.xml',
        "views/res_users_view.xml",
        'views/base_module_menus.xml',


    ],   

  
    "application": True,
}
