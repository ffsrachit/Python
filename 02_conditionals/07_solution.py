order_size = str(input("Please provide a size:"))
extra_shot = str(input("Yes OR No:"))


if extra_shot == "Yes":
    coffee = order_size + " coffee with extra shot"
else : 
    coffee = order_size + " coffee"

print("Order:" ,coffee)