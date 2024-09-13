l =int(input("input the value of l"))
F =int(input("input the value of F"))
n =int(input("input the value of n"))
w =int(input("input the value of w"))
s =int(input("input the value of s"))
P1 = F ** w
P2 = P1 * (((s * l) / F) + ((20 * n) / F))
P3 = 20 ** w
P4 = P3 + F ** (0.5)
Y = l - P2 / P4
print(Y)  