from data import menu, resources, coin_value, account


def check_coins():
    """Checks the value of the coins deployed"""
    return round(coin_value["quarter"] * quarters_entered + coin_value["dime"] * dimes_entered + coin_value[
        "nickel"] * nickels_entered + coin_value["penny"] * pennies_entered, 2)


def check_resources():
    """Checks if the resources are available before proceeding"""
    if user_input == "espresso":
        if resources["water"] <= 50:
            return "Sorry there is no enough water."
        if resources["coffee"] <= 18:
            return "Sorry there is no enough coffee."
        elif user_input == "latte":
            if resources["water"] <= 200:
                return "Sorry there is no enough water."
            if resources["coffee"] <= 24:
                return "Sorry there is no enough coffee."
            if resources["milk"] <= 150:
                return "Sorry there is no enough coffee."
        elif user_input == "cappuccino":
            if resources["water"] <= 250:
                return "Sorry there is no enough water."
            if resources["coffee"] <= 24:
                return "Sorry there is no enough coffee."
            if resources["milk"] <= 100:
                return "Sorry there is no enough coffee."


def check_trans():
    """Checks if the coins provided equals the cost and calculates the change"""
    if user_input == "espresso":
        if check_coins() >= menu["espresso"]["cost"]:
            change = round(check_coins() - menu["espresso"]["cost"], 2)
            print(f"Here is {change} in change.")
            account["money"].append(menu["espresso"]["cost"])
        else:
            print("Sorry that's not enough money. Money refunded.")
    elif user_input == "latte":
        if check_coins() >= menu["latte"]["cost"]:
            change = round(check_coins() - menu["latte"]["cost"], 2)
            print(f"Here is {change} in change.")
            account["money"].append(menu["latte"]["cost"])
        else:
            print("Sorry that's not enough money. Money refunded.")
    elif user_input == "cappuccino":
        if check_coins() >= menu["cappuccino"]["cost"]:
            change = round(check_coins() - menu["cappuccino"]["cost"], 2)
            print(f"Here is {change} in change.")
            account["money"].append(menu["cappuccino"]["cost"])
        else:
            print("Sorry that's not enough money. Money refunded.")


def check_prices():
    """Checks the coffee prices and prints the prices"""
    if user_input == "prices":
        print("Espresso: ", menu["espresso"]["cost"])
        print("Latte: ", menu["latte"]["cost"])
        print("Cappuccino: ", menu["cappuccino"]["cost"])


def make_coffee():
    """Makes the coffee, deducts the resources from and serves the user their coffee"""
    if user_input == "espresso":
        espresso_water = resources["water"] - menu["espresso"]["ingredients"]["water"]
        resources["water"] = espresso_water
        espresso_coffee = resources["coffee"] - menu["espresso"]["ingredients"]["coffee"]
        resources["coffee"] = espresso_coffee
        print("Here is your espresso ☕️. Enjoy!")
    elif user_input == "latte":
        latte_water = resources["water"] - menu["latte"]["ingredients"]["water"]
        resources["water"] = latte_water
        latte_milk = resources["milk"] - menu["latte"]["ingredients"]["milk"]
        resources["milk"] = latte_milk
        latte_coffee = resources["coffee"] - menu["latte"]["ingredients"]["coffee"]
        resources["coffee"] = latte_coffee
        print("Here is your latte ☕️. Enjoy!")
    elif user_input == "cappuccino":
        cappuccino_water = resources["water"] - menu["cappuccino"]["ingredients"]["water"]
        resources["water"] = cappuccino_water
        cappuccino_milk = resources["milk"] - menu["cappuccino"]["ingredients"]["milk"]
        resources["milk"] = cappuccino_milk
        cappuccino_coffee = resources["coffee"] - menu["cappuccino"]["ingredients"]["coffee"]
        resources["coffee"] = cappuccino_coffee
        print("Here is your cappuccino ☕️. Enjoy!")


def report():
    """Prints the resources and money report"""
    print("Water: ", resources["water"])
    print("Milk: ", resources["milk"])
    print("Coffee: ", resources["coffee"])
    print("Money: $", sum(account["money"]))


# While loop variable
machine_on = True
while machine_on:
    # Ask the user what they want.
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    check_prices()
    if user_input == "report":
        report()
    if user_input == "off":
        machine_on = False
    # a. Check the user’s input to decide what to do next.
    if user_input == "espresso" or user_input == "cappuccino" or user_input == "latte":
        check_resources()
        print("Please insert coins")
        quarters_entered = int(input("How many quarters?: "))
        dimes_entered = int(input("How many dimes?: "))
        nickels_entered = int(input("How many nickels?: "))
        pennies_entered = int(input("How many pennies?: "))
        check_coins()
        check_trans()
        make_coffee()
