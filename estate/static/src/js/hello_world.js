odoo.define(
    'hello_world.main', 
    function (require) {  const AbstractAction = require('web.AbstractAction');  
    const core = require('web.core');  
    const OurAction = AbstractAction.extend({  template: "action_hello_world",  info: "this message comes from the JS"});
    core.action_registry.add('hello_world.action', OurAction);});
    