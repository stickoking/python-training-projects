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
    "money": 0.0
}

coffee_type = ''
coffee_power = True

def prompt(resource, cost):
    global coffee_type
    global coffee_power
    
    water = resource["water"]
    milk = resource["milk"]
    coffee = resource["coffee"]
    money = resource["money"];
    request = input("What would you like? (espresso/latte/cappuccino): ")
    if request == "report":
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")
        return {'ingredients': ""}
    elif request == "espresso":
        coffee_type = 'espresso'
        return cost["espresso"]
    elif request == "latte":
        coffee_type = 'latte'
        return cost["latte"]
    elif request == "cappuccino":
        coffee_type = 'cappuccino'
        return cost["cappuccino"]
    elif request == "off":
        coffee_power = False
        return {'ingredients': ""}
    else:
        print("Incorrect Input")
        return {'ingredients': ""}
        

def resource_check(resource, ingredients):
    if ingredients == "":
        return False
    else:
        for item in ingredients:
            if resource[item] < ingredients[item]:
                print(f"Sorry there is not enough {item}")
                return False
            else:
                return True

def process_coins():
    quarter = 0.25
    dime = 0.10
    nickle = 0.05
    penny = 0.01

    quarter = quarter * int(input("How many quarters? :"))
    dime = dime * int(input("How many dimes?: "))
    nickle = nickle * int(input("How many nickles?: "))
    penny = penny * int(input("How many pennies?: "))

    return sum([quarter, dime, nickle, penny]) 

def transaction(coin, cost, resource):
    if coin < cost['cost']:
        print("Sorry that's not enough money. Money refunded.")
        return resource
    elif coin > cost['cost']:
        change = round(coin - cost['cost'], 2)
        print(f"Here is ${change} dollars in change.")
        return make_coffee(resource, cost)
    else:
        return make_coffee(resource, cost)

def make_coffee(resource, cost):
    temp_resources = resource
    ingredients = cost['ingredients']
    for item in ingredients:
        temp_resources[item] = temp_resources[item] - ingredients[item]
    temp_resources['money'] = temp_resources['money'] + cost['cost']
    return temp_resources

def coffee_machine(resources):
    temp_resources = resources
    coffee = prompt(resources, MENU)
    available_resources = resource_check(resources, coffee['ingredients'])
    if available_resources:
        coins = process_coins()
        temp_resources = transaction(coins, coffee, resources)
        print(f"Here is your {coffee_type} ☕️. Enjoy!")
    return temp_resources

while coffee_power:
    resources = coffee_machine(resources)
