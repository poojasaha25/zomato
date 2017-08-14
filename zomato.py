rest = {
    'Dominos':
        {
            'owner_name': 'abc',
            'rating':'4',
                      'menu':
            {
                'Country Special':400,
                'Farmhouse': 450,
                'Mexican Green Wave': 500,
                'Peppy Paneer': 430
            }
        },
    'KFC':
        {
             'owner_name': 'xyz',
             'rating':'5',
                     'menu':
            {
                'Popcorn': 100,
                'Chicken Zinger':  290,
                'Dips': 20,
                'Chicken Rockstar':  150
            }
        }
       }
#function to calculate bill
def bill_fun(price):
    bill=(price*0.1)+(price*0.6)+(price*0.15)+price
    return bill

d=rest['Dominos']['menu']
kfc=rest['KFC']['menu']

user_profile=raw_input("Enter \n 1.for restursnt owner \n 2: for customer")
if user_profile==  '1':
     owner_choice=raw_input("1 for update any information.\n 2: to update that information")
     if owner_choice=='1':
         res_choice=raw_input("enter which resturant  information you want to update 1:Dominos\n 2:KFC")
         if res_choice=='1':
             while True:
                dominos_update=raw_input("enter the food item")
                dominos_update_price=raw_input("enter the price:")
                to_end_loop=raw_input("1.If entries are complete \n 2.want to enter more information")
                if to_end_loop=='1':
                     break
                elif to_end_loop=='2':
                     continue
         elif res_choice=='2':
             kfc_update = raw_input("enter the food item")
             kfc_update_price = raw_input("enter the price:")


elif user_profile== '2':
    customer_choice=raw_input("1 to get details of the resturant  and  Place an order")
    if customer_choice== '1':
        cus_choice=raw_input("1.All the available resturant \n 2:Which cuisine you want to have \n 3:check in the list if food is available or not")
        if cus_choice=='1':
            resturant=rest.keys()
            print resturant
        elif cus_choice=='2':
            cus_choice_rest=raw_input("1.Dominos menu \n 2:KFC menu")
            if cus_choice_rest=='1':
                print d
            elif cus_choice_rest=='2':
                print kfc
        if cus_choice== '3':
             cus_choice1=raw_input("1.if  food is not available 2:if available ")
             if cus_choice1== '1':
                 print "sorry not available order something else"
             elif cus_choice1== '2':
                 delievery_choice = raw_input("1:for delievery  \n 2 for walk-in")
                 if delievery_choice == '1':
                    order_rest=raw_input("enter the resturant from which order is to be placed")
                    if order_rest in rest.keys():
                         food=raw_input("enter the food")
                         if food in rest[order_rest]['menu'].keys():
                             calculate_bill=rest[order_rest]['menu'][food]
                             print "delievery chosen and the bill is " ,calculate_bill
                 elif delievery_choice=='2':
                             order_rest = raw_input("enter the resturant from which order is to be placed")
                             if order_rest in rest.keys():
                                 food = raw_input("enter the food")
                                 if food in rest[order_rest]['menu'].keys():
                                    od=rest[order_rest]['menu'][food]
                                    finalbill=int(od)
                                    calculate_bill_1= bill_fun(od)
                                    print "your bill is",calculate_bill_1


rating=raw_input(" 1 if u wish to give rating \n 2:exit ")
if rating=='1':
    #Give rating to resturant as per user enter choice like press 1 if you wish to give rating to dominos and 2.if you want to rate KFC
    res_rate=raw_input("which resturant you wish to rate \n 1:Dominos /n 2:KFC")
    if res_rate=='1':
        rate=raw_input("enter your rating")
        rest['Dominos']['rating'] = rate
    elif res_rate=='2':
        rate1=raw_input("enter your rating")
        rest['KFC']['rating']=rate1
else:
    print "thankyou for visit"


