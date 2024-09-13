'''write a code that tests the values of x1 and x2 of a quadratic equation''' 
a = int(input("enter the value of a "))
b = int(input("enter the value of b "))
c = int(input("enter the value of c "))
x1 = int(input("enter the value the value of x1 "))
x2 = int(input("enter the value of x2 "))
testing_for_x1 = (a * (x1 ** 2) + (b * (x1)) + c)
# solve and confirm the result of x1, if the value of x1 is 0
if testing_for_x1 == 0 :
    print("the inputed root for x1 is correct")
else :
    print("the inputed root for x1 is wrong")
testing_for_x2 = (a * (x2 ** 2) +(b * (x2)) + c)
# solve and confirm the result of x2, if the value of x2 is -5
if testing_for_x2 == -5 :
    print("the inputed root for x2 is correct")
else :
    print("the inputed root for x2 is wrong")