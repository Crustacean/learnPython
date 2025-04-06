from menu import MENU as menu
#from prettytable import PrettyTable
#table = PrettyTable()

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}

coins = {

    "penny": 1,
    "nickel": 5,
    "dime": 10,
    "quarter": 25

}

def calculator(x):
    if x == 'p':
        return round((coins["penny"]/100), 2)
        
    elif x == 'n':
        return round((coins["nickel"]/100), 2)
        
    elif x == 'd':
        return round((coins["dime"]/100), 2)
        
    elif x == 'q':
        return round((coins["quarter"]/100), 2)
        
    

def get_water():
    return resources["water"]
    
def get_milk():
    return resources["milk"]
    
def get_coffee():
    return resources["coffee"]
    
def get_money():
    return resources["money"]

def get_report():
    
    water = get_water()
    milk = get_milk()
    coffee = get_coffee()
    money = get_money()
    
    #return "Water:\t" +str(water)+"ml" +"\nMilk:\t" +str(milk)+"ml" +"\nCoffee:\t" +str(coffee)+"g" +"\nMoney:\t$" +str(money)
    return water, milk, coffee, money

def print_report():
    water, milk, coffee, money = get_report()

    print("+---------------+--------------------+")
    print("| Resource Name | Current Quantities |")
    print("+---------------+--------------------+")
    print(f"| Water         | "+str(water)+"                |")
    print(f"| Milk          | "+str(milk)+"                |")
    print(f"| Coffee        | "+str(coffee)+"                |")
    print(f"| Money         | "+str(money)+"                |")
    print("+---------------+--------------------+")

    """print(table)

    table.add_column("Resource Name", ["Water", "Milk", "Coffee", "Money"])
    table.add_column("Current Quantities", [water, milk, coffee, money])
    table.align = "l" """

def get_resources(order):
    shortage_list = []
    order_ingredients = order["ingredients"]
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            shortage_list.append(item)
            
    if shortage_list:
        if len(shortage_list) > 1:
            shortage_string = ", ".join(shortage_list[:-1]) + " and " + shortage_list[-1]
        elif len(shortage_list) == 1:
            shortage_string = shortage_list[0]
        
        print(f"Sorry, there is'nt enough {shortage_string}.")
        return shortage_list, -1
            
    else:
        return None, order["cost"]
            
def place_order(order):
    if order == "espresso":
        resources["water"] -= menu["espresso"]["ingredients"]["water"]
        resources["coffee"] -=  menu["espresso"]["ingredients"]["coffee"]
        
    elif order == "latte":
        resources["water"] -= menu["latte"]["ingredients"]["water"]
        resources["milk"] -= menu["latte"]["ingredients"]["milk"]
        resources["coffee"] -= menu["latte"]["ingredients"]["coffee"]
        
    elif order == "cappuccino":
        resources["water"] -= menu["cappuccino"]["ingredients"]["water"]
        resources["milk"] -= menu["cappuccino"]["ingredients"]["coffee"]
        resources["coffee"] -= menu["cappuccino"]["ingredients"]["coffee"]
        
    else:
        return
        
def topup(shortage):
    if shortage == "water":
        resources["water"] = 300
    elif shortage == "milk":
        resources["milk"] = 200
    else:
        resources["coffee"] = 100
        
def process_order(drink, order, shortage, status):
    
    if status != -1:
        cost_None, cost = get_resources(drink)
        remaining_cost = cost
        total = 0
        
        print("Total cost: $"+str(cost))
        print("Enter Amount as letter P for 'penny', N for 'nickel', D for 'dime', Q for 'quarter' ")
        
        while remaining_cost > total:
            cash = input(f"Enter coins. Remaining $" + str(round(remaining_cost-total, 2)) +f" for your {order}! : ").lower()
            
            if len(cash) == 1 and cash in ['p', 'n', 'd', 'q']:
                coin_value = calculator(cash)
                total += coin_value
                print(round(total, 2))
            elif cash == "cancel":
                if total > 0:
                    print("Order cancelled. Your money is $" + str(round(total, 2)))
                get_order()
            else:
                print("Wrong coin. Enter Amount as letter P for 'penny', N for 'nickel', D for 'dime', Q for 'quarter' ")
            
        change = total - cost
        print("Your balance is $" + str(round(change, 2)))
        resources["money"] += cost
        
        place_order(order)
        print_report()

def get_order():
    
    on = True
    
    while on:
        
        order = input("What would you like? (espresso, latte, cappuccino): ")
    
        if order == "report":
            print_report()
            
        elif order in ["espresso", "latte", "cappuccino"]:
            drink = menu[order]
            shortage, status = get_resources(drink)

            if status != -1:            
                process_order(drink, order, shortage, status)
                
            elif status == -1:
                
                while len(shortage) != 0:
                    
                    for val in shortage:
                        ans = input(f"Would you like to top up the {val}? ( Yes or No) ").lower()
                        
                        if ans == "yes":
                            topup(val)
                            shortage.remove(val)
                        elif ans == "no":
                            print("Order cancelled.")
                            get_order()
                        elif ans == "report":
                            print_report()
                            
                    else:
                        continue
                        
                if len(shortage) == 0:
                    print_report()
                    process_order(drink, order, shortage, status)
                
        elif order == "off":
            print("Turning off the coffee machine.")
            on = False

        else:
            print("Invalid input. Please enter espresso, latte, cappuccino, report, or off.")
            
get_order()