'''write a script that solves a quadratic equation with two answers'''
a = int(input("input the value of a"))
b = int(input("input the value of b"))
c = int(input("input the value of c"))
P1 = -(b)
P2 = b ** 2 
P3 = 4 * a * c
P4 = ((P2) - (4 * a * c))** (0.5)
P5 = 2 * a
x1 = (P1 + P4) / P5
x2 = (P1 - P4) / P5 
print(x1)
print(x2) 