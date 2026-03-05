grade = int(input("Grade of student:"))

if(grade == 10):
    print("Please verify your grade")
    exit()

if grade >= 90:
    print("A")
elif grade >=80:
    print("B")
elif grade >=70:
    print("C")
elif grade >= 60:
    print("D")
else : 
    print("F")