MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 20,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 30,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 50,
    }
}

resources = {
    "water": 1000,
    "milk": 1000,
    "coffee": 500,
}

# -----------------  Variables ---------------------------

# Quarter = 0.25
# Dime = 0.10
# Nickle = 0.05
# Penny = 0.01

resource = [300, 200, 120]  # water, milk, coffee
money = 0
secret_password = "qwerty"


# --------------------------------------------------

# create a function which gets hold of all the ingredients and cost of the chosen drink

def drink_detail(drink_name):
    """ Get hold of ingredients of chosen drink"""

    drink = MENU[drink_name]["ingredients"]
    water = drink["water"]
    milk = drink["milk"]
    coffee = drink["coffee"]
    # cost = MENU[drink_name]["cost"]
    return [water, milk, coffee]  # not cost


# --------------------------------------------------------------------

def deduct_resources(drink):
    """ deducts the resources according to the consumption """
    for i in range(3):
        resource[i] = (resource[i] - drink_detail(drink)[i])
    global money
    money += MENU[drink]["cost"]


# -------------------------------------------------

def catch_money_error(currency_name):
    "checks error while entering money for eg: when entering a string"
    no_error_while_input_money = True
    while no_error_while_input_money:
        try:
            currency_name = float(input(f"How many {currency_name}? "))
            break
        except ValueError:
            print("\n please only type NUMBERS 🔢 \n")
            continue
    return currency_name


# ------------------------------------------------------------

def check_money(drink):
    """ Check the money received to fulfill the order"""
    print(" \n Please insert coins \n ")

    cost_of_drink = MENU[drink]["cost"]
    amount_received = (catch_money_error("quarters") * 0.25) + (catch_money_error("dimes") * 0.10) + (
                catch_money_error("nickles") * 0.05) + (catch_money_error("pennies") * 0.01)

    if amount_received == cost_of_drink:
        print(f"Here is your {drink} ☕. Enjoy 😊 \n")
        deduct_resources(drink)
    elif amount_received > cost_of_drink:
        print(
            f" \n Here is your ${round(amount_received - cost_of_drink, 2)} in change 💵 \n ")  # round upto 2 decimal places
        print(f"Here is your {drink} ☕. Enjoy 😊 \n")
        deduct_resources(drink)
    else:
        print(" \n Not enough money ❌ \n Money refunded \n")


# ------------------------------------------------------------------

def check_resource_sufficient(drink):
    """ Check enough resource to make the drink """
    can_make = True
    contents = ["water 💧", "milk 🥛", "coffee ☕"]

    for i in range(3):
        if resource[i] < drink_detail(drink)[i]:
            print(f" \n Sorry! there is not enough {contents[i]}")
            can_make = False
    return can_make


# --------------------------------------------------------------------


machine_on = True  # a boolean which keeps the coffee machine on


def admin_priviledges(choice):
    """ checks for admin priviledges """

    enter_password = input(
        " \n It requires Admin priviledges 🔒 \n Please confirm your identity by entering the password 🔑: ")
    if enter_password == secret_password:
        if choice == "report":
            print(
                f" \n Water: {resource[0]}ml \n Milk: {resource[1]}ml  \n  Coffee: {resource[2]}g \n Money: ${money} \n")
        else:
            global machine_on  # using global keyword to modify the global variables
            machine_on = False
            print(" \n Coffee shop is now closed. see you again 🚀 \n ")
    else:
        print(" \n Password is wrong! you can't perform the operation ❌ \n")


# --------------------------------------------------------------

def drink_cost(drink_name):
    """ Get hold of cost of drink, to display at the beginning """
    cost = MENU[drink_name]["cost"]
    print(f"\n The price of {drink_name} is ${cost} \n")
    wanna_buy = input(f"Do you wanna buy {drink_name}? Type 'y' or 'n':  ").lower()
    if wanna_buy == "n":
        return False  # not continue
    else:
        return True


# -----------------------------------------------------

while machine_on:
    choice = input(" \n What would you like? (espresso, latte, cappuccino) ?: ")

    if choice not in ["latte", "cappuccino", "espresso", "off", "report"]:
        print("\n Not available ❌ \n Tips: Try checking the spelling \n")
        continue
    elif choice == "off":
        admin_priviledges(choice)
    elif choice == "report":
        admin_priviledges(choice)
    # check resourse sufficient...
    else:
        # can provide the cost of that chosen drink
        if drink_cost(choice):
            if check_resource_sufficient(choice):
                check_money(choice)
        else:
            continue