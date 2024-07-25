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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#Espresso:
#   50ml water
#   18g Coffee
#Latte:
#    200ml water
#   24g Coffee
#   150ml Milk
#Cappuccino
#   250ml Water
#   24g Coffee
#   100ml Milk

#Starting stock
#   300ml water
#   200ml Milk
#   100g Coffee

#Program Requirements
#   TODO 1. Print Report
#   TODO 2. Check resources sufficient?
#   TODO 3. Process coins
#   TODO 4. Check transaction successful?
#   TODO 5. Make Coffee (deduct resources)

#var set
money = 0
profit = 0

customer_input = 0

#subtract resources
def subtract_resource(drink):
    global money
    #compare resources
    #subtract
    #else: say there is not enough of specific resource
    if resources["water"] >= MENU[drink]["ingredients"]["water"]:
        if resources["milk"] >= MENU[drink]["ingredients"]["milk"]:
            if resources["coffee"] >= MENU[drink]["ingredients"]["coffee"]:
                resources["milk"] -= MENU[drink]["ingredients"]["milk"]
                resources["water"] -= MENU[drink]["ingredients"]["water"]
                resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
                money += MENU[drink]["cost"]

                coin_count()

                print(f"Here is your {drink}. Enjoy!")

                ask_customer()
            else:
                print("Sorry there is not enough coffee")
                ask_customer()
        else:
            print("Sorry there is not enough milk.")
            ask_customer()
    else:
        print("Sorry there is not enough water.")
        ask_customer()

#counting coints
def coin_count():
    global money
    global profit
    #ask coin amount
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))

    #find total value in coins and compare
    quarters_val = quarters * 0.25
    dimes_val = dimes * 0.10
    nickles_val = nickles * 0.05
    pennies_val = pennies

    total_coin_amt = quarters_val + dimes_val + nickles_val + pennies_val

    if total_coin_amt > money:
        change = total_coin_amt - money
        print(f"Your change is ${change}")
        profit += money
        ask_customer()
    elif total_coin_amt == money:
        profit += total_coin_amt
        profit += money
        ask_customer()
    elif total_coin_amt < money:
        print("Sorry that's not enough money. Money refunded...")
        ask_customer()


#ask customer
def ask_customer():
    global customer_input
    global money

    money = 0
    customer_input =  input("What would you like? (espresso/latte/cappuccino): ")

    #order drinks
    if customer_input == "espresso":
        if resources["water"] >= MENU["espresso"]["ingredients"]["water"]:
            if resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
                resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
                money += MENU["espresso"]["cost"]

                coin_count()

                print("Here is your espresso. Enjoy!")

            else:
                print("Sorry there is not enough coffee")
                ask_customer()
        else:
            print("Sorry there is not enough water.")
            ask_customer()
    elif customer_input == "latte":
        subtract_resource("latte")
    elif customer_input == "cappuccino":
        subtract_resource("cappuccino")


    #shut down
    elif customer_input == 'off':
        print("Shutting down")
        quit()

    #Print report/receipt
    elif customer_input == 'report':
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${profit}")

        ask_customer()

    #in case typo/not valid drink
    else:
        print("Sorry, that is not a valid drink. Please try again.")
        ask_customer()

ask_customer()