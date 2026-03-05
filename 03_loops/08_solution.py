number = int(input("Please enter a number: "))
count = 0

for i in range(1, number + 1):
    if number % i == 0:
        count += 1

if count == 2:
    print(number, "is Prime")
else:
    print(number, "is not Prime")