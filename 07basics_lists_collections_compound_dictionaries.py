"""
--------------------------------------------
LISTS, COLLECTIONS AND COMPOUND DICTIONARIES
--------------------------------------------
"""

# list populated in the for loop
numbers = []
for i in range(1000):
    numbers.append(i)

print(len(numbers))
print(79*'-')

# comprehension list
numbers = [i for i in range(1000)]
print(len(numbers))

# comprehension created dictionary
print(79*'-')
keys_and_values = [(1, 'a'), (2, 'b'), (3, 'c')]
dictionary = {number: letter for (number, letter) in  keys_and_values}
print(dictionary)

# comprehension created set
print(79*'-')
numbers = {number for number in range(0, 10)}
print(numbers)