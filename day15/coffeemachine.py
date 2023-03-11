# Coffee Machine
import menu


def report():
    print(f"Water: {menu.resources['water']}ml")
    print(f"Milk: {menu.resources['milk']}ml")
    print(f"Coffee: {menu.resources['coffee']}ml")
    print(f"Money: ${menu.money}")


def check_resources(coffee_choice):
    coffee = menu.MENU[coffee_choice]
    ing_water = coffee["ingredients"]["water"]
    ing_coffee = coffee["ingredients"]["coffee"]
    ing_milk = 0

    if ("milk" in coffee["ingredients"]):
        ing_milk = coffee["ingredients"]["milk"]

    if (ing_water > menu.resources["water"]):
        print("Sorry there's not enough water.")
        return False

    if (ing_coffee > menu.resources["coffee"]):
        print("Sorry there's not enough coffee.")
        return False

    if (ing_milk > menu.resources["milk"]):
        print("Sorry there's not enough milk.")
        return False

    return True


def transact(coffee_choice):
    coffee = menu.MENU[coffee_choice]
    coffee_cost = coffee["cost"]

    print("=== ORDER SUMMARY ===")
    print(f"1 X {coffee_choice}")
    print(f"Amount: ${coffee_cost}")
    print("=====================")

    print("Please insert coins.")

    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    user_amount = (quarters * .25) + (dimes * .1) + \
        (nickles * .05) + (pennies * 0.01)

    if user_amount < coffee_cost:
        print(f"Sorry ${user_amount} is not enough money. Money refunded.")
        return False

    change = round(float(user_amount) - float(coffee_cost), 2)

    # Deduct from resource
    menu.resources['water'] -= coffee["ingredients"]["water"]

    if ("milk" in coffee["ingredients"]):
        menu.resources['milk'] -= coffee["ingredients"]["milk"]

    menu.resources['coffee'] -= coffee["ingredients"]["coffee"]
    # Add Sale
    menu.money += coffee_cost

    print(f"Here is ${change} in change.")
    print(f"Here is your {coffee_choice}. Enjoy!")

    return True


def coffee_machine():

    is_exit = False

    while not is_exit:

        choice = input(
            "What would you like? (espresso/latte/cappuccino): ").lower()

        if choice not in ("report", "espresso", "latte", "cappuccino"):
            print("Sorry you entered an invalid input.")
            is_exit = True
            break

        if choice == "report":
            report()
        elif choice in ("espresso", "latte", "cappuccino"):
            is_enough = check_resources(choice)
            if is_enough:
                transact(choice)
        else:
            is_exit = True
            break


coffee_machine()
