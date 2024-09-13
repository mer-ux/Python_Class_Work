name = input("Enter your name")
age = int(input("Enter your age"))
if age >= 0 and age <= 10 :
    print("access not granted")
    print("check again next year")
elif age >= 11 and age <= 17 :
    print("access granted")
    print("enter kid lounge")
elif age >= 18 and age <= 120 :
    print("access granted")
    print("enter main hall")
else :
    print("enter the right age")