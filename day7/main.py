MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
is_machine_on = True


def is_resource_sufficient(order_ingredients):
    """Returns the true when order can be made or false when cant be made"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough ingredients of {item}")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted"""
    print("please insert coin.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_recieve, drink_cost):
    """Return True when the payment is accepted or return False when declined"""
    if money_recieve < drink_cost:
        print("Sorry, that's not enough money, money refunded!")
        return False
    else:
        global profit
        profit += money_recieve
        change = round(money_recieve - drink_cost, 2)
        print(f"here is {change} dollars in change")
        return True


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    print(f"Your {drink_name} is being made.")
    for item in resources:
        resources[item] -= order_ingredients[item]


while is_machine_on:
    customer_drink = input("what would you like? (espresso/latte/cappuccino) ")
    if customer_drink == "off":
        is_machine_on = False
    elif customer_drink == 'report':
        print(f"water:{resources['water']}ml")
        print(f"milk:{resources['milk']}ml")
        print(f"coffee:{resources['coffee']}g")
        print(f"profit:{profit}")
    else:
        drink = MENU[customer_drink]
        # {
        #     "ingredients": {
        #         "water": 200,
        #         "milk": 150,
        #         "coffee": 24,
        #     },
        #     "cost": 2.5,
        # },
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(customer_drink, drink["ingredients"])
