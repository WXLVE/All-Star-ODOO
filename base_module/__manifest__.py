{
    "name": "Cube",  # The name that will appear in the App list
    "version": "16.0",  # Version
    "application": True,  # This line says the module is an App, and not a module
    'depends': [
        "base",
        'website',
        'web',
        
    ],  # dependencies

    'data': [
        'security/ir.model.access.csv',
        'views/cube_property_views.xml',
        'views/cube_menus.xml',
        'views/cube_types.xml',
        'views/cube_tags.xml',
        'views/res_users_view.xml',
        'views/cube_offers.xml',

        'views/snippets/testSnippet.xml',
    ],
    'assets': {
        'web.assets_frontend': [

            'base_module/static/src/snippets/sidebar/sidebarstyle.css',
            'base_module/static/src/images/orange_checkmarkSmall.png',
        ],
    },

    "installable": True,
    'license': 'LGPL-3',

}