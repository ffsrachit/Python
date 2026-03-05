items = ["apple", "banana", "orange", "apple", "mango"]

unique = set()

for i in items:
    if i in unique:
        print("Duplicate:", i)
        break
    else:
        unique.add(i)