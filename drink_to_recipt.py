"""
This is dedicated to the Most Sacred Heart of Jesus, 
the Immaculate Heart of Mary 
and the Chaste Heart of St. Joseph
"""
import random

header = "receipt_id, drink_id, ice, sweetness, milk, boba, popping_boba\n"

#50% chance one drink ordered per receipt
#25% chance two drinks
#25% chance three drinks

with open("drink_to_recipt.csv", "w") as file:
    file.write(header)

    for i in range(0,600):
        rowString = f"{i+1000}, {random.randint(0,14)}, Normal, {100}, Cow, False, False\n"
        file.write(rowString)

        if random.randint(0,1) == 0:
            rowString = f"{i+1000}, {random.randint(0,14)}, Normal, {100}, Cow, False, False\n"
            file.write(rowString)

            if random.randint(0,1) == 0:
                rowString = f"{i+1000}, {random.randint(0,14)}, Normal, {100}, Cow, False, False\n"
                file.write(rowString)

        

        
