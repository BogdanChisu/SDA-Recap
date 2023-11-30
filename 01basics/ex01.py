"""
Ex. 1
-----
Write a program (or function) that will compare the area/price ratio between
two pizzas. In order to calculate the area of a circle P at a given radius r
"""
# from math import pi
#
# dictionary_sizes = {
#     32: 15,
#     36: 20
# }
#
# ratios = []
#
# def circle_area_to_price(dict):
#     for item in dict.keys():
#         area = pi * dict[item] ** 2
#         ratios.append(area / dict[item])
#
#     max_ratio = max(ratios)
#     max_index = ratios.index(max_ratio)
#
#     return f'Max area to price ratio for: ' \
#            f'{list(dictionary_sizes.items())[max_index]}'
#
# print(circle_area_to_price(dictionary_sizes))

"""
Ex. 2
-----
Write a program that checks if a given number is preceded by a prime number.
"""
# from math import sqrt
# def preceeded_by_prime(a_number):
#     for i in range(2, int(sqrt(a_number - 1) + 1)):
#         if a_number % i == 0:
#             return f'The number {a_number} is not preceeded by a prime'
#     return f'The number {a_number} is preceeded by a prime'
#
# print(preceeded_by_prime(4))
# print(preceeded_by_prime(16))
# print(preceeded_by_prime(24))

"""
Ex. 3
Write a function (or program) that will calculate the zeros of the given square
function. For this purpose, you can use the formulas presented here.
"""
# from math import sqrt
#
# def calculate_zeros_sq_function():
#     a = float(input("Please input the coefficient for x^2, a = "))
#     b = float(input("Please input the coefficient for x, b = "))
#     c = float(input("Please input the coefficient for x^0, c = "))
#
#     if a == 0:
#         return f'The solution of the equation is {-b / c}'
#
#     delta = b * b - 4 * a * c
#
#     if delta > 0:
#         print("Two solutions")
#         print(f'x_1 = {(-b + sqrt(delta)) / (2 * a)}')
#         print(f'x_2 = {(-b - sqrt(delta)) / (2 * a)}')
#
#     elif delta == 0:
#         print("one solution")
#         print(-b / 2 * a)
#
#     elif delta < 0:
#         print("no solution")
#
# calculate_zeros_sq_function()

"""
Ex. 4
-----
Write a function (or program) that will correctly display the sentence "Alice 
has x cats" depending on the number of cats. 
That is it can show: 
Alice has 1 cat, 
Alice has 2 cats, 
Alice has 10 cats.
"""
#
# def print_cat_msg(cats):
#     if cats == 1:
#         return f'Alice has {cats} cat.'
#     return f'Alice has {cats} cats.'
#
# print(print_cat_msg(5))
# print(print_cat_msg(1))
# print(print_cat_msg(0))

"""
Ex. 5
-----
Write a program that will display the given sentence. Every third one will be 
capitalized and every fourth one will have an exclamation mark at the end. 
(Just don't tell lies!;)
"""

# def repeat_sentences(sentence, repetitions):
#     for i in range(repetitions):
#         if (i + 1)  % 3 == 0:
#             print(i, ' ', sentence.upper())
#         elif (i + 1) % 4 == 0:
#             print(i, ' ', sentence, '!')
#         else:
#             print(i, ' ', sentence)
#
# repeat_sentences("Thou shal not steal", 20)

"""
Ex. 6
-----
Aaaaaa - that means 6.
Write a function (or program) that will determine the number of vowels in a 
given string.
"""

# def print_vowels_count(some_string):
#     i = 0
#     for letter in some_string:
#         if letter in "AEIOUaeiou":
#             i += 1
#     print(f'The string: {some_string} has {i} vowels')
#
# print_vowels_count('Power Overwhelming!')

"""
Ex. 7
-----
Pick 10 numbers from 0 to 10. If any number repeats, display the message: 
Oh no! I repeated myself!
"""

# from random import randint
#
# def draw_ten_random():
#     array_nr = []
#     for i in range(10):
#         nr = randint(0, 10)
#
#         if nr in array_nr:
#             print(f"Oh no! I repeated myself! {nr}")
#         else:
#             print(f"Lucky number: {nr}")
#
#         array_nr.append(nr)
#
# draw_ten_random()

"""
Ex. 8
-----
Write a function (or program) that will flatten the tensor into a 
one-dimensional list. Tensor - definition.
Given tensor:
```python
tensor = [[[1,2,3],[1,2,3],[1,2,3]],
[[1,2,3],[1,2,3],[1,2,3]],
[[1,2,3],[1,2,3],[1,2,3]]]
"""

# def tensor_to_vector(tensor):
#     list_a = []
#     for i in tensor:
#         for j in i:
#             for k in j:
#                 list_a.append(k)
#     print(list_a)
#
# tensor = [
#     [[1,2,3],[1,2,3],[1,2,3]],
#     [[1,2,3],[1,2,3],[1,2,3]],
#     [[1,2,3],[1,2,3],[1,2,3]]
# ]
#
# tensor_to_vector(tensor)

"""
Ex. 9
-----
Write a function (or program) that will check if the given PESEL has the 
correct checksum.
"""

# def check_pesel(pesel_nr):
#     if len(str(pesel_nr)) != 11:
#         return False
#     pesel_list = [int(nr) for nr in str(pesel_nr)]
#     factors = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
#     checksum = sum([a * b for a, b in zip(pesel_list[:-1], factors)])
#     control_number = 10 - pesel_list[-1]
#     if control_number != (checksum % 10):
#         return False
#
#     return True
#
# print(check_pesel(12345678901))
# print(check_pesel(12345678903))

"""
Ex. 10
------
Write a program that lists the files in a given directory and adds an ordering
number to the end of the file name.

###Note The file extension must remain unchanged! Use the library of os.
"""

# import os
#
# def numerate_files(filepath):
#     for index, file in enumerate(os.listdir(filepath)):
#         list_fname = file.split('.')
#         list_fname[0] = list_fname[0] + "_" + str(index)
#         os.rename(os.path.join(filepath, file),
#                   os.path.join(filepath, f'{list_fname[0]}.{list_fname[1]}'))
#
# numerate_files('other/')

"""
Ex. 11
------
Task 2: Let's turn the world upside down.
Write a function (or program) that will display a text from any text file while:
-changing lowercase letters to uppercase. -uppercase to lowercase letters.
"""

# def change_case(filename):
#     with open(filename) as f:
#         lines = f.readlines()
#         for line in lines:
#             new_line = line.swapcase()
#             print(new_line)
#
# change_case('other/file_0.txt')

"""
Ex. 12
------
OOP Basics

Design a Rational class representing rational numbers as pairs of integers (
a numerator and a denominator).

The class shoud contain magic methods that define the following 
functionalities:
- the comparison methods: eq, lt, gt, le, ge, cmp
- the operators +, -, *, / should be implemented correctly and return a new 
  object of this class
- the comparison methods should take 1/2 = 2/4
- the float method should return a decimal number, and int should be similar to
  its counterpart in the case of float numbers. Additionally, the invert 
  method should be used.
- it should be possible to save the current result to a file and load it.

- the class should always try to keep the abbreviated version of the fraction.
"""
from math import gcd
import json

class Rational:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.to_irreducible_fraction()

    def to_irreducible_fraction(self):
        greatest_common_divisor = gcd(self.numerator, self.denominator)
        while greatest_common_divisor != 1:
            self.numerator = self.numerator // greatest_common_divisor
            self.denominator = self.denominator // greatest_common_divisor
            greatest_common_divisor = gcd(self.numerator, self.denominator)

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        else:
            return str(self.numerator) + "/" + str(self.denominator)

    def __repr__(self):
        items = (f"{k}={v}" for k, v, in self.__dict__.items())
        return f"{self.__class__.__name__}({', '.join(items)})"

    def __add__(self, other):
        numerator = self.numerator * other.denominator + \
                    self.denominator * other.numerator
        denominator = self.denominator * other.denominator

        return Rational(numerator, denominator)

    def __sub__(self, other):
        numerator = self.numerator * other.denominator - self.denominator * \
                    other.numerator
        denominator = self.denominator * other.denominator

        return Rational(numerator, denominator)

    def __mul__(self, other):
        return Rational(self.numerator * other.numerator, self.denominator *
                        other.denominator)

    def __truediv__(self, other):
        return self * ~other

    def __lt__(self, other):
        return self.__cmp__(other) < 0

    def __le__(self, other):
        return self.__cmp__(other) <= 0

    def __gt__(self, other):
        return self.__cmp__(other) > 0

    def __ge__(self, other):
        return self.__cmp__(other) >= 0

    def __eq__(self, other):
        return self.__cmp__(other) == 0

    ## Compare two numbers
    def __cmp__(self, other):
        temp = self - other
        if temp.numerator > 0:
            return 1
        elif temp.numerator < 0:
            return -1
        else:
            return 0

    def __invert__(self):
        return Rational(self.denominator, self.numerator)

    def __float__(self):
        return self.numerator/self.denominator

    def __int__(self):
        return int(float(self))

    def save(self):
        json.dump(self, )

    def load(self):
        json.load()

number1 = Rational(16, 32)

print(f'Number1: {number1}')