from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

inp = input('enter your drink espresso latte ')
is_on = True
drink = menu.find_drink(inp)

res_sufficient = coffee_maker.is_resource_sufficient(drink)

while is_on:
    options = menu.get_items()
    choice = input(f'what would you like{options}')
    if choice == 'off':
        is_on = False
    elif choice =='report':
        coffee_maker.report()
        money_machine.report()
    else:
         drink = menu.find_drink(choice)
         if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
             coffee_maker.make_coffee(drink)
