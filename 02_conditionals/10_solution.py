type = str(input("Please give type of animal"))
age = int(input("Please give age"))

if type == "dog" and age <=2 :
    food = "Puppy food"
elif type == "cat" and age >= 5:
    food = "Senior Cat food"
else : food = "Regular food"

print("food is :", food)