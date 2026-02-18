"""
This is dedicated to the Most Sacred Heart of Jesus, 
the Immaculate Heart of Mary 
and the Chaste Heart of St. Joseph
"""

header = "id, name, ice, sweetness, milk, boba, popping_boba, price\n"
drinkVarieties = {
    "0": {"name": "Black Milk Tea", "ice_level": "Normal","sweetness": "100", "milk": "Cow", "boba": "False", "popping_boba": "False", "price":7.50},
    "1": {"name": "Green Milk Tea", "ice_level": "Normal","sweetness": "100", "milk": "Cow", "boba": "False", "popping_boba": "False", "price":7.50},
    "2": {"name": "Matcha Milk Tea", "ice_level": "Normal","sweetness": "100", "milk": "Cow", "boba": "False", "popping_boba": "False", "price":7.50},
    "3": {"name": "Taro Milk Tea", "ice_level": "Normal","sweetness": "100", "milk": "Cow", "boba": "False", "popping_boba": "False", "price":7.50},
    "4": {"name": "Jasmine Milk Tea", "ice_level": "Normal","sweetness": "100", "milk": "Cow", "boba": "False", "popping_boba": "False", "price":7.50},
    "5": {"name": "Oolong Milk Tea", "ice_level": "Normal","sweetness": "100", "milk": "Cow", "boba": "False", "popping_boba": "False", "price":7.50},
    "6": {"name": "Thai Milk Tea", "ice_level": "Normal","sweetness": "100", "milk": "Cow", "boba": "False", "popping_boba": "False", "price":7.50},
    "7": {"name": "Black Tea", "ice_level": "Normal","sweetness": "100", "milk": "None", "boba": "False", "popping_boba": "False", "price":7.50},
    "8": {"name": "Green Tea", "ice_level": "Normal","sweetness": "100", "milk": "None", "boba": "False", "popping_boba": "False", "price":7.50},
    "9": {"name": "Matcha Tea", "ice_level": "Normal","sweetness": "100", "milk": "None", "boba": "False", "popping_boba": "False", "price":7.50},
    "10": {"name": "Taro Tea", "ice_level": "Normal","sweetness": "100", "milk": "None", "boba": "False", "popping_boba": "False", "price":7.50},
    "11": {"name": "Jasmine Tea", "ice_level": "Normal","sweetness": "100", "milk": "None", "boba": "False", "popping_boba": "False", "price":7.50},
    "12": {"name": "Oolong Tea", "ice_level": "Normal","sweetness": "100", "milk": "None", "boba": "False", "popping_boba": "False", "price":7.50},
    "13": {"name": "Thai Tea", "ice_level": "Normal","sweetness": "100", "milk": "None", "boba": "False", "popping_boba": "False", "price":7.50},
    "14": {"name": "Chocolate Milk", "ice_level": "None","sweetness": "100", "milk": "Cow", "boba": "False", "popping_boba": "False", "price":7.50}
}

with open("drink.csv", "w") as file:
    file.write(header)

    for (id,drink) in drinkVarieties.items():
        idString = f"{id}, "
        file.write(idString)

        for attribute in drink:
            drinkString = f"{drink[attribute]}"


            #if last attribute of drink, add newline character
            if attribute == "price":
                drinkString += "\n"
            else:
                drinkString += ", "

            file.write(drinkString)

#DONE :)