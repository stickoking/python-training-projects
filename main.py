from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
coffee = menu.get_items()
is_on = True

while is_on:
    user_choice = input(f"What would you like ({coffee}): ")
    if user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_choice == "off":
        is_on = False
    else:
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink):
            if(money_machine.make_payment(drink.cost)):
                coffee_maker.make_coffee(drink)


