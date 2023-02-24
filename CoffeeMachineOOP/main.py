from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMaker = CoffeeMaker()
menu = Menu()
register = MoneyMachine()
items = menu.get_items()

is_on = True
while is_on:
    choice = input(f'What would you like? ({items})')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(coffeeMaker.report())
        print(register.report())
    else:
        drink = menu.find_drink(choice)
        if coffeeMaker.is_resource_sufficient(drink) and register.make_payment(drink.cost):
            coffeeMaker.make_coffee(drink)