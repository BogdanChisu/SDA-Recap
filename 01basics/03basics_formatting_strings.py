"""
-------------------------------------------------------------------------------
The print function explained
-------------------------------------------------------------------------------
"""

print("What", "a", "beautiful", "day", sep="-", end="!\n")

"""
-------------------------------------------------------------------------------
1. Formatting the old way
-------------------------------------------------------------------------------
Strings in Python have a unique built-in operation that can be accessed 
using the % operator. This makes it easy to perform simple formatting. The 
value given after the string or subsequent values given in the data are 
substituted for the percent sign in the string.
"""
name = "Bob"
print('Hello, % s!' % name)
"""
- the %s format tells Python to substitute the value of the name represented as
  a string (s in %s is derived from a string).
  ----------------
  %s - string
  %d - number
  %x - converts the decimal to hexadecimal representation
"""
number = 42
print('My favorite number is: %d' % number)

error = 4637
print('Error number: %x' % error)

"""
-------------------------------------------------------------------------------
2. Formatting strings str.format() - the newer solution
-------------------------------------------------------------------------------
It allows changing the display order of the parameters without changing the 
arguments passed to the format() method.
"""
name = "Bob"
number = 42
error = 46372518

print('Listen, {name}, your number is {number} and the code is {code}'.
      format (name = name, number = number, code = error))

title = "General"
name = "Kenobi"
print("Hello there, {1} {0}". format (title, name))

"""
-------------------------------------------------------------------------------
3. Interpolation of f-string - the newest solution
-------------------------------------------------------------------------------
"""
a = 2
b = 7
print(f"{a} times {b} to the power of 2 {(a * b) ** 2}.")
"""
Formatting also allows the user to add a specific number of spaces to the 
left or right of the string (this option is also available in previous ways 
of formatting the strings):
"""
header_name = "Name"
header_age = "Age"
name = "John"
age = 22

print(f"| {header_name:10} | {header_age:10} |")
print("-" * 27)
print(f"| {name:10} | {age:10} |")

# you can also define how many digits after the decimal point should be
# displayed or display the number as a percentage:

n = 109.98437824238490
print(f"{n:.3f}") # 109.984

percentage = 0.71
print(f"{percentage:.1%}") # 71.0%