from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

is_on = True
while is_on:
    choose = input(f"What drinks would you like to get {menu.get_items()}? ")
    if choose == "report":
        money_machine.report()
        coffee_maker.report()
    elif choose == "off":
        is_on = False
    elif choose == "":
        while choose == "":
            choose = input(f"Please choose something or type 'off' to turn off the machine: ")
            if choose == "off":
                is_on = False
                break
    else:
        drink = menu.find_drink(choose)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
