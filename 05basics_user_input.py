"""
---------------------
The input() function
---------------------
"""
# print("Hello")
# user_name = input("What is your name: ")
# print(f"Hi, {user_name}")

"""
The input function will always return a string.
To avoid the problem you need to convert to the desired data type:
"""
# age = int(input('Please input your age: '))
# age += 1
# print(f'Next year you will have... {age} years')

"""
-----------------------
Command line parameters 
-----------------------
"""

import sys

print(sys.argv[0]) # the first argument is always the file path
print(sys.argv[1])
print(sys.argv[2])

"""
To execute you will have to call the program from the command line:
python my-program.py first_arg second_arg
"""
