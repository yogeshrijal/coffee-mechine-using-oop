from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money_count=MoneyMachine()
coffee_maker=CoffeeMaker()
is_on=True
menu=Menu()
while is_on:
    option=menu.get_items()
    coffee=str(input(f"what do you like: {option}").lower())
    if coffee=="off":
        is_on=False
    elif coffee=="report":
        money_count.report()
        coffee_maker.report()
    else:
        drink=menu.find_drink(coffee)
        resource=coffee_maker.is_resource_sufficient(drink)
        if resource==False:
            print("insufficent resource")
        else:
            print(money_count.make_payment(drink.cost))
            coffee_maker.make_coffee(drink)



















