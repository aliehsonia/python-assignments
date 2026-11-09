print("welcome to CATUC POS")

num_items =int(input("enter number of items:"))
items = []
items_cost_total =0
for item in range(1, num_items +1):
    description =input("enter item name: ")
    quantity =int(input("enter quantity: "))
    unit_price =float(input("enter unit price: "))
    total_price =quantity*unit_price
    items_cost_total=total_price
    items.append([item,description,quantity,unit_price,total_price])
print("\nRECIEPT")
print("S/N Description quantity unit price total price")

for item in items:
    print(f"{item[0]}\t  {item[1]}\t  {item[2]}\t  {item[3]: .2f}\t {item[4]: .2f}")
print("total expenditure: ",items_cost_total,"frs")
print("THANKS FOR YOUR PATRONAGE ")
    

