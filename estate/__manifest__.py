# -*- coding: utf-8 -*-

{
    'name': 'Apples',
    'description': "Where Pears become Apples" , 
    'depends': [
        'base',
        'web',
    ],
    
    
  'data': [
        
        #security
        # 'security/crm_security.xml',
        'security/ir.model.access.csv',


        #views,
        'views/estate_apple_offers.xml',
        'views/estate_apple_tags.xml',
        'views/estate_apple_types.xml',
        'views/estate_apple_views.xml',
        "views/res_users_view.xml",
        'views/estate_menus.xml',



    ],
    "application": True,
}


# {
#     "name": "Real Estate",
#     "category": 'Real Estate/Brokerage',
#     "depends": [
#         "base",
#         "web",
#     ],
#     "data": [
#         #Security
#         "security/ir.model.access.csv",
#         'security/crm_security.xml',
#         #Views
#         "views/estate_property_offer_views.xml",
#         "views/estate_property_tag_views.xml",
#         "views/estate_property_type_views.xml",
#         "views/estate_property_views.xml",
#         "views/res_users_views.xml",
#         "views/estate_menus.xml",
        
#         'views/estate_apple_views.xml',
#         'views/estate_menus.xml',
#     ],
#     #Is it a Applcation?
#     "application": True,
# }