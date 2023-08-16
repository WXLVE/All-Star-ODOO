import urllib.request
import odoorpc

def synchronize_data(data):
    test_data = [185, 15, 13]
    data_list = []
    ########################### DATABASE 1 ###########################
    
    ## Atttempt to CONNECT
    try:
        pwd_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
        pwd_mgr.add_password(None, "http://example.net", "userName", "passWord")
        auth_handler = urllib.request.HTTPBasicAuthHandler(pwd_mgr)
        opener = urllib.request.build_opener(auth_handler)
        odoo_enterprise = odoorpc.ODOO('nhmbsoftware-test-1-8922164.dev.odoo.com', port=80, opener=opener)
        print(odoo_enterprise.version)
    except:
        print("DATABASE 1 Connection FAILED !  DATABASE NAME: nhmbsoftware-test-1-8922164")
        return 
    ##################################################################


    ########################### DATABASE 2 ###########################

    ## Atttempt to CONNECT
    try:
        pwd_mgr2 = urllib.request.HTTPPasswordMgrWithDefaultRealm()
        pwd_mgr2.add_password(None, "http://example.net", "userName", "passWord")
        auth_handler2 = urllib.request.HTTPBasicAuthHandler(pwd_mgr2)
        opener2 = urllib.request.build_opener(auth_handler2)
        odoo_intern = odoorpc.ODOO('intern.nhmbsoftware.nl', protocol='jsonrpc+ssl', port=443, opener=opener2)
        print(odoo_enterprise.version)
    except:
        print(" DATABASE 2 Connection FAILED !  DATABASE NAME: nhmbsoftware-test-1-8922164")
        return  
    ##################################################################

    #################### LOGIN ATTEMPT DATABASE 1 ####################
    try:
        odoo_enterprise.login('nhmbsoftware-test-1-8922164', 'daniel@nhmbsoftware.nl', 'daniel')
    except: 
        print(" Database 1 Login failed DATABASE NAME: NHMB-Intern, USER: daniel@nhmbsoftware.nl ")
        return 

    ##################################################################

    #################### LOGIN ATTEMPT DATABASE 2 ####################
    try:
        odoo_intern.login('nhmb-intern', 'daniel@nhmbsoftware.nl', 'daniel')
    except: 
        print(" Database 2 Login failed DATABASE NAME: NHMB-Intern, USER: daniel@nhmbsoftware.nl ")
        return
    ##################################################################


    #################### USERS ARE DEFINED HERE ! ####################
    
    user1 = odoo_enterprise.env.user
    user2 = odoo_intern.env.user
    print(user1)
    

    ##################################################################
    
    #################### ATTEMPTING DATA RETRIEVAL ###################


    try:
        for i in data:
            Lead = odoo_intern.env['crm.lead']
            try: 
                Lead.search([('id', '=' , i)])
                
                order_id = Lead.browse(i)
                # print(order_id)
                # print(order_id.name)
                # print(order_id.partner_id.name)
                # print(order_id.description)
                small_data = [order_id.id, order_id.name, order_id.partner_id, order_id.description]
                
                if data_list == "" or None:
                    data_list = [small_data]
                    
                else:
                    data_list = data_list + [small_data]
                    
                print(" ")
                print(data_list)
                
                print(" ")
            except:
                print("ERROR DATA IS NOT CORRECT")
                return

        
    except:
        print("WHOOPS, You Shouldn't Be Here !")
        return
        
        
    # try:
    #     for u in data_list:
    #         print("id: " + str(u[0]))
    #         print("name: " + str(u[1]))
    #         print("partner name: " + str(u[2]))
    #         print("description: " + str(u[3]))
    #         print("")
    #     # print(u[2])
    #     # for x in u:
    #     #     print(x)
    #     #     print('')
    
    # except:
    #     print("Something is not right")
    #     return
    ids_not_done = 0
    leads = odoo_enterprise.env['crm.lead']
    partners = odoo_enterprise.env['res.partner']
    # try:
    print(len(data_list))
        
        
    for i in data_list:
        print(i[2]['name'], '\n', i[2]['phone'])
        if not partners.search([('name', '=', i[2]['name'])]):
            print("partner did not exist, creating...")
            partners.create({'name': i[2]['name'], 'display_name': i[2]['display_name'], 'comment': i[2]['comment'], 'contact_address': i[2]['contact_address'],'email': i[2]['email'],'email_formatted': i[2]['email_formatted'],'email_normalized': i[2]['email_normalized'],'lang': i[2]['lang'], 'phone': i[2]['phone'], 'phone_sanitized': i[2]['phone_sanitized'], 'street': i[2]['street'], 'city': i[2]['city'], 'zip': i[2]['zip'] })
            
            # new_partner = partners.browse(name = i[2]['name'])
            new_partner = partners.search([('name', '=', i[2]['name'])])
            new_partner_found = partners.browse(new_partner)
            print(new_partner, '\n', new_partner_found)
            
            print("new partner spotted, creating a new oppurtunity!")
            leads.create({'name': i[1], 'partner_id': new_partner_found.id, 'description': i[3]})

        else:
            expected_result = partners.search([('name', '=', i[2]['name'])])
            print(expected_result)
            found_partner = partners.browse(expected_result)
            print(found_partner)
            print(found_partner.id)
            
            if not leads.search([('name', '=', i[1])]):
                
                print("opportunity did not exist, creating a new one...")
                leads.create({'name': i[1], 'partner_id': found_partner.id, 'description': i[3]})
            else:
                id_of_existing_lead = leads.search([('name', '=', i[1] )])
                print(id_of_existing_lead)
                chosen_data = leads.browse(id_of_existing_lead)
                print(chosen_data)
                if chosen_data.name == i[1] and chosen_data.description == i[3]: # HERE WE CHECK IF ALL KNOWN FIELDS HAVE THE SAME VALUES
                    ids_not_done += 1
                    continue
                else:   # IF NOT ALL FIELDS HAVE THE SAME VALUES
                        # WE UPDATE ALL FIELDS
                        chosen_data.name = i[1]
                        chosen_data.description = i[3]
                        print("updating found oppurtunity...")
                    

    # print("total times data up-to-date: " + ids_not_done)
        

    
    

# synchronize_data(test_data)


    # WHAT DO WE NEED
    #   res.partner
    #   naam
    #   description
    #   mail.message.body
    #   mail.message.author_id
    #   mail.message.create_id
    #   mail.message.res_id



