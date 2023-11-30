"""
-------------------------
if, if-else, if-elif-else
-------------------------
"""
#
# x = 0
# y = 3
#
# if x > y:
#     print(f"{x} is greater than {y}")
#
# if x < y:
#     print(f"{x} is less than {y}")

# The else clause
# ---------------

# x = 0
# y = 3
#
# if x > y:
#     print(f'{x} is greater than {y}')
# else:
#     print(f'{y} is greater than {x}')

# The elif clause
# ---------------

x = 0
y = 3

if x > y:
    print(f'{x} is greater than {y}')
elif x == 3:
    print(f'{x} is equal to {y}')
else:
    print(f'{x} is less than {y}')

print('This line is always printed')

"""
--------------
The while loop
--------------
"""

n = 0
while n < 5:
    n += 1
    print(n)

# break and continue
# ------------------

n = 0
while n < 5:
    n += 1
    if n == 4:
        break
    if n == 1:
        continue
    print(n)

"""
------------
The for loop
-----------
"""

animals = ["Dog", "Cat", "Fish"]

for animal in animals:
    print(animal)

"""
--------------------
The range() function
--------------------
"""

for i in range(3):
    print(i)

for i in range(-3, 1):
    print(i)

for number in range(3, 11, 2):
    print(number)

print(79*'-')

for number in range(-1, -4, -1):
    print(number)

"""
------------------------
The enumerate() function
------------------------
"""
print(79*'-')
fruits = ["apple", "banana", "lemon"]

for index, fruit in enumerate(fruits):
    print(f"Fruit: {fruit}, has index: {index}")