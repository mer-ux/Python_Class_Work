
'''
#
# AUGMENTED ASSIGNMENT OPERATOR

a = 1 + 2
a = 3

b = 1 + 3 
b = 3

b +=3 # b = b + 3

a  -= 2 # a = a - 2

'''
'''
i = 1 # Declaring a variable
while i < 6: 
    print(i)
    i -= 1 # i = i + 1
    print("loop continues")
print("end of loop")

'''
'''
i = 1 
while i < 6:
  print(i)
  if i == 3:
    break #stops here once i is 3.
  i += 1
  '''
'''
import time
i = 0#, 1, 2
while i < 10000:
  i += 1
  if (i%10) == 0:
    print('ALarm Alarm Alarm')
    time.sleep(5)
    continue
  print(i)
'''
'''
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

'''
'''
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  # x = 'cherry'
  print(x)
'''
'''
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

'''

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in range(1,13):
  for y in range(1,13):
    print(f'{x} x {y} = {x * y}')