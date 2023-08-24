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

    ],
    # 'js': [
    #     'static/src/js/jquery-3.6.0.min.js',
    #     'static/src/js/velocity.min.js',
    #     'static/src/js/velocity.ui.min.js',
    # ],
    'assets': {
        'web.assets_frontend': [
            # Carousel
            'base_module/static/src/snippets/s_sliding_carousel/carousel.css',
            'base_module/static/src/snippets/s_sliding_carousel/000.js',
            
        ],
    },
    "application": True,
}
