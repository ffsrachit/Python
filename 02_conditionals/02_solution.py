age = int(input("Please give me a age:"))

day = str(input("Please give me a day:"))

if age >=18:
    price = 12
else :
    price = 8

if day ==  "Wednesday" : 
    price -= 2

print("Ticket price for you is $", price)