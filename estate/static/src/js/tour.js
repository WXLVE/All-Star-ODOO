
odoo.define('apple.tour', function (require) {
    'use strict';

    var core = require('web.core');
    var tour = require('web_tour.tour');

    var _t = core._t;

    tour.register('apple_tour', {
        url: "/web",
        display_name: _t("Apple Tour"),
        tour_summary: _t("Discover the features of Apple"),
        steps: [
            {
                title: _t("Main Menu"),
                content: _t("Welcome to the main menu of Apple module!"),
                element: '.o_app[data-menu-xmlid="apple.menu_apple_root"]',  // Main menu selector
            },
            {
                title: _t("Tree View"),
                content: _t("This is the tree view of Apple module."),
                element: '.o_list_view.o_app[data-menu-xmlid="apple.menu_apple_root"] .o_list_record:first',  // Tree view record selector
            },
            {
                title: _t("Create Button"),
                content: _t("Click the 'Create' button to open the create form."),
                element: '.o_list_view.o_app[data-menu-xmlid="apple.menu_apple_root"] .o_list_button_add',  // Create button selector
            },
            {
                title: _t("Create Form"),
                content: _t("This is the create form of Apple module."),
                element: '.o_form_view.o_app[data-menu-xmlid="apple.menu_apple_root"]',  // Create form selector
            },
        ],
    });

});
