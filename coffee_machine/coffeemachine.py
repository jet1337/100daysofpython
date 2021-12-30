# Coffee Machine
# Simulate a coin-operated coffee vending machine user experience

import math
import time

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

drinks = {
    "E": "espresso",
    "L": "latte",
    "C": "cappuccino"
}

# adjust values to accommodate for more drinks
resources = {
    "water": 400,
    "milk": 250,
    "coffee": 100,
}


# Get a status of the remaining resources by inputting "report"
def print_report():
    """
    Print a report on the resources currently in the machine
    :return:
    """
    print(f"""
Resources Remaining
-Water: {resources["water"]}mL
-Milk: {resources["milk"]}mL
-Coffee: {resources["coffee"]}mL
""")


def check_resources(drink):
    """
    Check if the machine has resources for the selected drink
    :param drink:
    :return: Bool for available resources
    """
    can_make = True
    if resources["water"] < MENU[drinks[drink]]["ingredients"]["water"]:
        can_make = False
    elif resources["coffee"] < MENU[drinks[drink]]["ingredients"]["coffee"]:
        can_make = False
    if drink in ["L", "C"]:
        if resources["milk"] < MENU[drinks[drink]]["ingredients"]["milk"]:
            can_make = False
    return can_make


def process_coins(cost):
    """
    User will continue to input coins until they meet the required amount for drink\n
    Call coin_return() to dispense change if too much money input\n
    :param cost: Make the user add coins until they reach the cost of the drink
    :return: Bool for drink being paid, Float for money inserted into machine
    """
    coins = [".01", ".05", ".10", ".1", ".25"]
    money = 0
    print("Enter coins one at a time in any order")
    print("Only '.25' '.1' '.05' and '.01' supported\nEnter nothing to stop payment")
    while not successful_trans(cost, money):
        current_coin = input("$")
        # user wants to quit
        if current_coin == "":
            # return any coins input to user
            return False, money
        # input validation for coins only
        elif current_coin not in coins:
            print("\nOnly Enter '.25' '.1' '.05' or '.01'\n")
            continue
        else:
            current_coin = round(float(current_coin), 2)
            money += current_coin
            print(f"Remaining: ${round(cost - money, 2)}")
    # drink was paid for
    return True, money


def coin_return(money):
    """
    Take the change and return it to the user in coins via print statement
    :param money:
    :return:
    """
    q = math.floor(money / .25)
    money -= .25 * q
    d = math.floor(money / .10)
    money -= .10 * d
    n = math.floor(money / .05)
    money -= .05 * n
    p = round(money / .01)
    print(coin_return_string(q, d, n, p))


def coin_return_string(q, d, n, p):
    """
    Build a grammatically correct string for the coin_return function
    :param q: number of quarters
    :param d: number of dimes
    :param n: number of nickles
    :param p: number of pennies
    :return: Formatted string
    """
    final_string = f"The machine returns"
    if q == 1:
        final_string += f" {q} quarter,"
    else:
        final_string += f" {q} quarters,"
    if d == 1:
        final_string += f" {d} dime,"
    else:
        final_string += f" {d} dimes,"
    if n == 1:
        final_string += f" {n} nickle,"
    else:
        final_string += f" {n} nickles,"
    if p == 1:
        final_string += f" and {p} penny.\n"
    else:
        final_string += f" and {p} pennies.\n"
    return final_string


def successful_trans(cost, money):
    """
    Checks to see that the transaction was successful
    :param cost: Cost of drink
    :param money: Currently inserted coins
    :return:
    """
    if money < cost:
        return False
    else:
        return True


def dispense(drink):
    """
    'Dispense' the drink for the user
    :param drink:
    :return:
    """
    selection = drinks[drink]
    print(f"\nThe machine pops out a cup, and begins filling it with {selection}.")
    resources["water"] -= MENU[selection]["ingredients"]["water"]
    resources["coffee"] -= MENU[selection]["ingredients"]["coffee"]
    if drink in ["L", "C"]:
        resources["milk"] -= MENU[selection]["ingredients"]["milk"]
    # delay for user experience
    for i in range(3):
        print(". ", end="")
        time.sleep(1)
    print(f"\nYour {drinks[drink]} is ready!")


def main():
    drink = ""
    print("""
Thank you for choosing our vending machine!
Our drink options are as follows:
    Espresso (E) - $1.50
    Latte (L) - $2.50
    Cappuccino (C) - $3.00
    """)
    while drink != "Q":
        drink = input("Which drink would you like?\nChoices: 'E' 'L' or 'C' (Enter 'Q' to quit): ").upper()
        # input validation
        if drink == "REPORT":
            print_report()
            continue
        if drink not in ["E", "L", "C", "Q"]:
            print("Enter a valid choice...\n")
            continue
        if drink == "Q":
            break
        # check the current resources for the desired drink
        while True:
            can_make = check_resources(drink)
            # not enough resources available
            if not can_make:
                print(f"\nNot enough resources for {drinks[drink]}.\n")
                break
            else:
                drink_cost = MENU[drinks[drink]]['cost']
                print(f"\nThe cost of {drinks[drink]} is ${'{:.2f}'.format(drink_cost)}.\n")
                drink_paid, inserted_money = process_coins(drink_cost)
                # drink was paid for
                if drink_paid:
                    dispense(drink)
                    if inserted_money > drink_cost:
                        coin_return(inserted_money - drink_cost)
                    else:
                        print("\nExact change given - No coins were returned\n")
                else:
                    print("No drink was dispensed.")
                    if inserted_money > 0:
                        coin_return(inserted_money)
                break


if __name__ == "__main__":
    main()
