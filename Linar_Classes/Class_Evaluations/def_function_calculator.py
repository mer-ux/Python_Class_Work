'''Write a code that solves six operations, using the "if" statement and a comparism operation to breakdown each operation individually'''

def simultaneous_equation(a, b, c):
     #a = int(input("input the value of a "))
     #b = int(input("input the value of b "))
     #c = int(input("input the value of c "))
     P1 = -(b) 
     P2 = b ** 2 
     P3 = 4 * a * c
     P4 = (P2 - P3)** (0.5)
     P5 = 2 * a
     x1 = (P1 + P4) / P5
     x2 = (P1 - P4) / P5 
     return x1 , x2

def subtraction(value_1, value_2 ):
    #value_1 = int(input("enter the first value: "))
    #value_2 = int(input("enter the second value: "))
    answer = value_1 - value_2
    return answer


def addition(value_1, value_2):
    #value_1 = int(input("enter the first value: "))
    #value_2 = int(input("enter the second value: "))
    answer = value_1 - value_2
    return answer


def multiplication(value_1, value_2) :
    #value_1 = int(input("enter the first value: "))
    #value_2 = int(input("enter the second value: "))
    answer = value_1 * value_2
    return answer


def division(value_1, value_2) :
    #value_1 = int(input("enter the first value: "))
    #value_2 = int(input("enter the second value: "))
    answer = value_1 / value_2
    return answer


def exponentional(value_1 , value_2) :
    #value_1 = int(input("enter the first value: "))
    #value_2 = int(input("enter the second value: "))
    answer = value_1 ** value_2
    return answer


print("welcome to my calculator, this calculator performs six operations")
operators = input("kindly choose the operator you want to work with from the given operators below \n a= addition \n b= subtraction \n c= multiplication \n d= division \n e= exponential \n f= quadratic \n")
# this operation uses the addition operator to sum two values
if operators == "a":
    print(addition(value_1 = int(input("enter the second value: ")),  value_2 = int(input("enter the second value: "))))
# this operation subtracts the second operand from the first operand
elif operators == "b":
    print(subtraction(value_1 = int(input("enter the second value: ")),  value_2 = int(input("enter the second value: "))))
# this operation multiplies both values
elif operators == "c" :
    print(multiplication(value_1 = int(input("enter the first value: ")),value_2 = int(input("enter the secon value: "))))
    # in this operation, the first operand is divided by the  second operand
elif operators == "d" :
    print(division(value_1 = int(input("enter the first value: ")),value_2 = int(input("enter the second value: "))))
    # this operation multiplies the first value by the  number of the second value
elif operators == "e" :
    print(exponentional(value_1 = int(input("enter the first value: ")), value_2 = int(input("enter the second value: "))))
    # this operation helps to calculate quadratic equation after providing the value of a, b and 
elif operators == "f" :
    print(simultaneous_equation(a = int(input("input the value of a ")),b = int(input("input the value of b ")), c = int(input("input the value of c "))))