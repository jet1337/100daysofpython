from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import sys


def main():
    my_menu = Menu()  # create a new menu
    coffee = CoffeeMaker()  # create a new coffee maker
    money = MoneyMachine()  # create a new money machine
    print("Welcome to the coffee vending machine!")
    while True:
        print("Our current options are as follows...")
        print(my_menu.get_items())
        selection = input("What option would you like?: ").lower()
        print()
        # Get the MenuItem
        current_item = my_menu.find_drink(selection)
        if selection == "report":
            print("\nCurrent Machine Status:\n")
            money.report()
            coffee.report()
            print()
        elif selection == "off":
            print("\nPowering off...")
            sys.exit(100)
        # check if selection is a drink
        elif current_item:
            # check if resources are available
            if coffee.is_resource_sufficient(current_item):
                # process the money
                if money.make_payment(current_item.cost):
                    # dispense the drink
                    coffee.make_coffee(current_item)


if __name__ == "__main__":
    main()
