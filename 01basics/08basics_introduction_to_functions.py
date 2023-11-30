"""
---------------------
Some simple functions
---------------------
"""
def print_hello_world():
    print("Welcome to your first function!")

def greet_by_name(name):
    print(f"Hi, {name}!")

print_hello_world()
greet_by_name("John")

"""
--------------------------
Function Naming Convention
--------------------------

Snake case is the standard for function names:
- good_function_name
- add_ingredients
- save_content_to_file


---------------------------------
Function Parameters and Arguments
---------------------------------

Function parameters can be:
- obligatory,
- optional (parameters named).
"""

def print_full_name(name, surname):
    print(f'{name} {surname}')

print(79*'-')
print_full_name('Jon', 'Snow')
print_full_name(name='Jon', surname='Snow')
print_full_name('Snow', surname='Jon')
print(79*'-')

# Types in Functions
# ------------------

# Python gives you the ability to define the types of argument and the
# return types

def print_hello(text: str) -> None:
    print(f"Hello {text}")

print_hello("world")

def get_hello(text: str) -> str:
    return f'Hello {text}'

print(get_hello('world'))

# Default Parameters
# -------------------

def greet_by_name(name="World!"):
    print(f'Hello, {name}')

print(79*'-')
greet_by_name()
greet_by_name('John')
greet_by_name(name='John')

# ---------------------------------------
# Functions with any number of arguments
# ---------------------------------------
def add(*args):
    result = 0
    for arg in args:
        result += arg
    return result

print(79*'-')
print(add(1, 2, 3, 4, 5))

def print_name_and_strings(name, *strings):
    print(f'Name: {name}')
    for string in strings:
        print(string)

print(79*'-')
print_name_and_strings("Jack", "a", "b", "c", "d")

#--------------------------------------------
# Function with any number of named arguments
#--------------------------------------------
def add_ingredients(**kwargs):
    result = 0
    for key in kwargs:
        result += kwargs[key]
    return result
print(79*'-')
print(add_ingredients(eggs=3, spam=5, cheese=2))

#-----------------------------------------------------------
# Function with any number of positional and named arguments
#-----------------------------------------------------------

def add_ingredients(*args, **kwargs):
    result = 0
    for arg in args:
        result += arg
    for key in kwargs:
        result += kwargs[key]
    return result

print(79*'-')
print(add_ingredients(1, 2, 3, eggs=3, spam=5, cheese=2))