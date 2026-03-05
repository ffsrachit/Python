distance = int(input("Please give a distance:"))

if distance <= 3:
    activity = "Walk"
elif distance <=15:
    activity = "Bike"
else: activity = "Car"

print(activity)