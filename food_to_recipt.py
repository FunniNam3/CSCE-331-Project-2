import random


# Header based on the food_to_receipt table in the DB diagram
header = "food_id, receipt_id, modifiers\n"


with open("food_to_receipt.csv", "w") as file:
    file.write(header)
    # Assuming 100 receipts (matching the drink_to_receipt range)
    for i in range(0, 600):
        if random.random() > 0.5:
            continue

        # First food item (Replace 10 with total number of food items you have)
        rowString = f"{random.randint(0,2)}, {i+1000}, null\n"
        file.write(rowString)
        if random.randint(0, 1) == 0:
            rowString = f"{random.randint(0,2)}, {i+1000}, null\n"
            file.write(rowString)
            if random.randint(0, 1) == 0:
                rowString = f"{random.randint(0,2)}, {i+1000}, null\n"
                file.write(rowString)

