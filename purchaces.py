import random

suppliers = [
    "Shahid Daniela",
    "Widya Betty",
    "Wali Nadine",
    "Valentin Zénaïde",
    "Coba Danyal",
    "Noah Dorotheos",
    "Korrine Tria",
    "Wellington Hisako",
    "Dikla Severo",
    "Viveka Ema"
]

contacts = [
    "(769) 342-4488",
    "(860) 370-1650",
    "(312) 259-5404",
    "(361) 513-6103",
    "(707) 328-2297",
    "(639) 569-6579",
    "(708) 133-3560",
    "(808) 781-9534",
    "(316) 987-5090",
    "(281) 095-9815"
]

with open("purchaces.csv", "w") as file:
    file.write("item_id, buy_date, supplier_name, supplier_contact, amount, supplier_price,\n")
    for x in range(random.randint(100,300)):
        supplierIndex = random.randint(0,len(suppliers)-1)
        item = f"{random.randint(0,100)}, {str(random.randint(1,12)) + "-" + str(random.randint(1,31)) + "-" + str(random.randint(2012, 2026))}, {suppliers[supplierIndex]}, {contacts[supplierIndex]}, {random.randint(10,100)}, {random.random() * 20},\n"
        file.write(item)