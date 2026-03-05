password = input("Please enter your password: ")

if len(password) <= 6:
    print("Your password is weak")
elif len(password) <= 10:
    print("Your password is medium")
else:
    print("Your password is strong")