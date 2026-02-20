
# not many food options so randomization not needed
foodVaraieties = [
    {"item": "BBQ pork", "price": 9.99},
    {"item": "Teriyaki chicken", "price": 9.99},
    {"item": "French fries", "price": 3.50}
]

with open("data/food.csv", "w") as file:
    file.write("id, item, amount\n")
    for id, food in enumerate(foodVaraieties, start=1):
        file.write(f"\n{id},{food['item']},{food['price']}")
        file.flush()
