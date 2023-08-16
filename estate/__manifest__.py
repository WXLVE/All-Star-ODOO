# -*- coding: utf-8 -*-

{
    'name': 'Apples',
    'description': "Where Pears become Apples" , 
    'depends': [
        'base',
        'web',
        "web_tour",
        'web_map',
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
        # "views/apple_assets.xml",
        # 'views/hello_world_views.xml'

    ],
  
    'qweb': [
        # 'estate/static/src/xml/hello_world.xml',
        "estate/static/src/js/components/PartnerOrderSummary.xml"
            
            ],
  
     'assets': { 
         'web.assets_backend': [
            #  'estate/static/src/js/hello_world.js',
            #  'estate/static/src/js/tour.js',
            #  'estate/static/src/css/hello_world.css',
             'estate/static/src/js/components/PartnerOrderSummary.js', 
         ] 
     },
    

  
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
