'''Write a code that solves six operations, using the "if" statement and a comparism operation to breakdown each operation individually'''
print("welcome to my calculator, this calculator performs six operations")
operators = input("kindly choose the operator you want to work with from the given operators below \n a= addition \n b= subtraction \n c= multiplication \n d= division \n e= exponential \n f= quadratic \n")
# this operation uses the addition operator to sum two values
if operators == "a" :
    value_1 = int(input("enter the first value: "))
    value_2 = int(input("enter the second value: "))
    answer = value_1 + value_2
   # print(answer)
    print("the addition of " + str(value_1) + " and " + str(value_2 ) + " is " + str(answer))
# this operation subtracts the second operand from the first operand
elif operators == "b" :
    value_1 = int(input("enter the first value: "))
    value_2 = int(input("enter the second value: "))
    answer = value_1 - value_2
    #print(answer)
    print("the subtraction of " + str(value_1) + " and " + str(value_2 ) + " is " + str(answer))
# this operation multiplies both values
elif operators == "c" :
    value_1 = int(input("enter the first value: "))
    value_2 = int(input("enter the secon value: "))
    answer = value_1 * value_2 
    #print(answer)
    print("the multiplication of " + str(value_1) + " and " + str(value_2 ) + " is " + str(answer))
# in this operation, the first operand is divided by the  second operand
elif operators == "d" :
    value_1 = int(input("enter the first value: "))
    value_2 = int(input("enter the second value: "))
    answer = value_1 / value_2
    #print(answer)
    print("the division of " + str(value_1) + " and " + str(value_2 ) + " is " + str(answer))
# this operation multiplies the first value by the  number of the second value
elif operators == "e" :
    value_1 = int(input("enter the first value: "))
    value_2 = int(input("enter the second value: "))
    answer = value_1 ** value_2
    #print(answer)
    print("the exponential of " + str(value_1) + " and " + str(value_2 ) + " is " + str(answer))
# this operation helps to calculate quadratic equation after providing the value of a, b and c
elif operators == "f" :
    a = int(input("input the value of a "))
    b = int(input("input the value of b "))
    c = int(input("input the value of c "))
    P1 = -(b)
    P2 = b ** 2 
    P3 = 4 * a * c
    P4 = ((P2) - (4 * a * c))** (0.5)
    P5 = 2 * a
    x1 = (P1 + P4) / P5
    x2 = (P1 - P4) / P5 
    #print(x1)
    #print(x2) 
    print("the roots of the provided quadratic equation is " + str(x1) + " or " + str(x2))
else :
    print("enter valid operation")   