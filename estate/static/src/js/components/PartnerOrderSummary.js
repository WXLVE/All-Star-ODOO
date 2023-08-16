odoo.define("estate.PartnerOrderSummary", function (require) { 
  
    const FormRenderer = require("web.FormRenderer"); 
    const { Component } = owl; 
    const { ComponentWrapper } = require("web.OwlCompatibility"); 
    const {
        onError,
        onMounted,
        onWillDestroy,
        useExternalListener,
        useRef,
        useState,
        useSubEnv,
        reactive,
    } = owl;
 
 
    /** 
     * OWL component responsible for displaying a partner order summary widget 
     * which will show order history details about a specific customer. 
     */ 
    // const { useState } = owl; 
  
    class PartnerOrderSummary extends Component { 
        partner = useState({}); 
     
        constructor(self, partner) { 
            super(); 
            this.partner = partner;
        } 
    }  
 
    /** 
     * Register properties to our widget. 
     */ 
    Object.assign(PartnerOrderSummary, { 
        template: "estate.PartnerOrderSummary" 
    }); 
 
    /** 
     * Override the form renderer so that we can mount the component on render 
     * to any div with the class o_partner_order_summary. 
     */ 
    FormRenderer.include({ 
        async _renderView() { 
            await this._super(...arguments); 
     
            for(const element of this.el.querySelectorAll(".o_partner_order_summary")) { 
                this._rpc({ 
                    model: "res.partner", 
                    method: "read", 
                    args: [[this.state.data.partner_id.res_id]] 
                }).then(data => { 
                    (new ComponentWrapper( 
                        this, 
                        PartnerOrderSummary, 
                        useState(data[0]) 
                    )).mount(element); 
                }); 
     
            } 
        } 
    }); 
});  

  