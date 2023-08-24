# -*- coding: utf-8 -*-
{
    'name': 'Website Builder IO',
    'description': "This a Example Module",
    'depends': [
        'digest',
        'web',
        'web_editor',
        'website',
    ],
    'data': [
        # Snippet Views
        'views/snippets/s_sliding_carousel.xml',
        'views/snippets/velo_slider.xml',

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
    'js': [
        'static/src/js/jquery-3.6.0.min.js',
        'static/src/js/velocity.min.js',
        'static/src/js/velocity.ui.min.js',
    ],
    'assets': {
        'web.assets_frontend': [
            # Carousel
            'base_module/static/src/snippets/s_sliding_carousel/carousel.css',
            'base_module/static/src/snippets/s_sliding_carousel/000.js',
            
        ],
    },
    "application": True,
}
