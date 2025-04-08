from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def place_order():
    
    money_machine = MoneyMachine()
    coffee_maker = CoffeeMaker()
    menu = Menu()
    
    coffee_maker.report()
    money_machine.report()
    
    is_on = True
    
    while is_on:

        available_drinks = menu.get_items()
    
        choice = input("Enter your drink. Select among "+available_drinks+" :")
        
        if choice in available_drinks.split("/"):
            drink = menu.find_drink(choice)
        
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
                        
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
            
        elif choice == "off":
            print("Turniong off coffee machine.")
            is_on = False            
    
place_order()