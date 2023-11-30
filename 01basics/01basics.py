"""
COMPUTER PROGRAMMING - is the process of designing, developing, testing and
source code maintenance of computer programs or micro-processors devices
(micro-controllers)

SOURCE CODE is written in a programming language governed by a specific rule set
and syntax. sometimes programming language can be a superset of another
programmng language (by expanding a programming language while keeping all its
functionalities). Programming utilizes concepts like application design,
algorithms, data structures, compilers and how computer hardware operates.

INTERPRETER is a program which analyzes source code and executes it. It speaks
directly to the machine, before any program is executed. Program code
interpretation is slower than compiled code execution. The interpreter has to go
through each command first and then assign actions to it. Compiled code only
executes actions as it has already been analyzed during the compilation phase.
There's no need to do it again.

COMPILER translates command to binary code.

PYTHON LANGUAGE PROFILE - easy to use and learn - Python is focused on creating
good source code in a fast manner. It's developer friendly and supports fast
code writting

    - White space case sensitive - the code aggregates in code blocks by using
        white spaces.

    - High-level - in terms of syntax, key words and the way program is created
        minimizes (or eliminates) the need to deal with computer hardware
        subtleties.

    - Interpreted - we don't need to compile the program. Python uses it's own
        interpreter

    - Dynamically typed - there's no need to provide data type in variable
        declaration, Python will guess the type of a variable.

    - Support for many programming styles (paradigms):
        - object (classes, methods, inheritance)
        - function (lambda expressions)
        - imperative (loops)
        - reflection(view variables, modules, classes) during program execution

    - Substantial standard library - Python provides many libraries (pre-coded
    functionalities that are available in Python to make program development
    faster and easier)

    - Freeware


------------------
PYTHON HISTORY
------------------
    - Created  by Guido van Rossum
    - Officially released in February 1991
    - 16th January 1994, first final version released
    - Python 3.0 is currently the only updated and supported Python version.
    - The name does not come from the snake but from "Monty Python's Flying
      Circus"

      Based on Stacked Overflow Developer Survey in 2019, Python was the most
      popular living language. It's even more popular than Java. Artificial
      Intelligence (AI) dynamic developent and web technologies can be
      contributed to its growth as well.

PYTHON USE CASES
-----------------

- Artificial intelligence and machine learning (Scikit-learn, Tensorflow)
    - recognition of objecrs in a photo (faces, vehicles, etc)
    - human language analysis, i.e. automatic text summary, a chat bot
    - forecasting phenomenons
    - learning how to play games
- Websites development /web technologies
    - web applications (Django, Flask)
    - REST API - site engine (requestsm BeautifulSoup)
- Data management and formatting (pandas, numpy)
    - read csv and xlsx files
    - fill in missing data, data cleansing
    - data analysis and visualization (charts, histograms)
- Testing (unittest, pytest)
    - unit, component and integration tests
- Task automation
    - creating automated bids for auctions
    - network or computer group management
- DevOps practice
    - improving the quality of software implementation
    - more frequent release of new code versions
    - better insight into processes and requirements

-----------------------------------------
First Program: The Hello, World! program
-----------------------------------------

Use the system console
-----------------------

As Python is an interpreted language, it provides a command console which can
execute a single command without running the whole program. You can test
Python's commands before you use them in your code.

To execute Python's command line, go to the system console (cmd, Powershell,
bash) and write a command:
"""

print("Hello, World!")

"""
How the program works
---------------------

- The command shows "Hello, World!" on the screen
- The built-in function print was used to achieve this
- This function uses the parameters in brackets i.e. the sentence, that we want
  to display on the screen.

At this point we can treat this function as a behavior: something needs to be
done depending on the parameter provided. A coffee machine is a good example. A
specific type of coffee is prepared (function) based on the user
choice(parameter).

----------
DATA TYPES
----------

What is a data type?
--------------------

A data type is a description of the type, structure and range of values that can
be assigned to a variable, constant, argument, fucntion result or a value.

Data types in Python
--------------------

All data in Python has its own type:

- int - the integer numbe type
- float - floating point number (real) type
- complex - complex number type
- str - text sequence type
- bool - boolean data type
- NoneType - specific, undefined type, null value

Integer Numbers
----------------

Usually called integers or ints. These are positive or negative numbers without
a decimal point (including 0) with infinite range.

Unlike static programming languages, Python dynamically allocates free space in
the machine's memory and assigns values which give access to them when needed.
That's why we can analyse large numbers in Python without worrying about memory
overflow.

In Python we can store numbers in: the decimal and the binary (0b prefix), the
octal (0o prefix) or the hexadecimal (0x prefix) system.

Below you will find the number 10 in several numerical systems: >>> 10 10
    >>> 0b1010
10
    >> 0o12
10
    >> 0xA
10


Floating Point Numbers
-----------------------

These include numbers with a decimal point: 1.5, 1.333, -10.0.

Floating point number data type is float. Python uses 8 bytes (64 bits) to store
the number value, so we can store with accuracy up to 15 digits after the
decimal point.

IMPORTANT! - The integer part is separated by a dot, not a comma. Also you
should not use floating point numbers for financial calculations, where accuracy
is important. In the binary system we cannot set the exact value of all numbers,
but the approximate value. You can avoid this using specific libraries like the
decimal.

Complex numbers
---------------

These numbers contain two parts: real and imaginary. They are stored with the
suffix j (like in electronics), instead of the one used in mathematics i.

Text data (string)
------------------

The str type is used to store text data i.e. a unicode string. Values of the
byte type are also text data, which allow to choose the coding format as needed.
Strings should be limited by quotes, or apostrophes (you should not use both in
the same code, it's good practice to stick to one format).

As you can see there are several ways to store text. The command starts a new
line.

In case we need to use an apostrophe or quotation marks as a value we need the
escape character \. This informs Python that we want to display these
characters. Otherwise Python will cut off values

>>> "Block \"Python basics\" is OK!"
    'Block "Python basics" is OK!'

Logic type (boolean)
--------------------

Variables of boolean type can take of two possible values: True or False.

Boolean data is often used in conditional instructions and loops.

None type
---------

None value is Python's way to represent something that is empty (when a variable
has no assigned value).

------------------
Checking data type
------------------

Easy to do using the "type" function The function uses parameters the same way
that "print" does.

---------------
TYPE CONVERSION
---------------

int(value) - convert data type <value> to int type. If the value is of a float
type, it cuts off the fractional part. 

float(value)

str(value)

bool(value)

complex(value)

----------------------
VARIBLES AND OPERATORS
----------------------

What is a variable?
-------------------
A variable is programming construction that has three basic attributes: 1 a
symbolic name, 2 storage location 3 a value

Variable declaration
--------------------
Variable declaration is done by assigning a name and a value to the variable by
using the '=' character.

    number = 10 word = "sentence" big_number = 99999.999 truth = True

The general pattern to define a variable in Python is presented below:

<variable_name> = <variable_value>

Types of variables
-------------------
Python is a dynamically typed language. This means that a variable type is
determined when we assign a value to it. If we assing an integer to a variable,
its type will be inferred from its value and set to int. If we assign a string
to the same variable, its type will change to str:

a = 5 print(type(a))  # prints <class 'int'>

a = 'iam string'

print(type(a))  # prints <class 'str'>

Python version 3.5 introduced the ability to specify types. Over the course of
subsequent versions, the way of specifying types has evolved but the idea has
not changed. Unlike Java, typing in Python is more of a suggestion than a rigid
declaration. This is a very important sequence because it has several
consequences. Let's first look at the syntax:

number: int = 5

So the type is placed after the colon that follows the variable's name. As this
is only a suggestion, Python will not stop us from doing something like this:

number: int = 'i am string'

print(type(number)) # prints <class 'str'>


Variable naming convention - the rules
--------------------------------------

Due to some restrictions, we are not able to name our variables as we please.
There are some ground rules, that should be followed when creating variables:

- You can change a variable's value by assigning a new value to it.
- A variable's name can use only letters a-z, A-Z, numbers 0-9, and the symbol _
- Lowercase and uppercase is important!
- A variable's name cannot begin with a number!

Permitted names:
    SUPER_VARIABLE = 1 bestVariableEver123 = "OK" _my_name = "Alice"
    next1_variable2 = 5.5 _____ = True

Prohibited names:
    123variable = 2 wrong$name%123 = False !@AlmOStGoODone!@ = None 12345 =
    "bad_name" VARIABLE-1 = 0

Variable naming styles
----------------------

There are several naming styles. Their popularity is so high, that the style
name is enough to recognize what can be expected in a project in terms of
variable naming convention.

- camel case (camel) style - it is named after camel humps. When a variable's
  name consists of more than one word, we start with a lowercase letter and then
  we add the next word beginning with an uppercase letter (important: white
  spaces are forbidden).

  veryLongString = "A String that is supposed to be very long... Something went
  wrong"

- upper camel case - similar to the other camel case. It begins with an
  uppercase letter (this one is mostly used for naming classes)

  VariableNameInUpperCamelCase = 1000

- snake case style - it's similar to the other camel case. The only difference
  is that the name begins with an uppercase letter (this one is used in Python
  for naming classes).

  snake_variable = 50.5

---------------
Variable Scope
---------------

Scope variables can be divided into:

- global variables - available in the entire file where it was declared
- local variable - available only in a specific block (function, method class)
  in which it was declared

Key words
---------

Key words are reserved for Python only. They cannot be used for variables,
functions or class names. Otherwise Python will return an error.

and         as          assert      async   await       break class continue def
del     elif        else except      False       finally for from        global
if          import      in          is      lambda None nonlocal    not or
pass    raise       return True try while       with    yield

--------------------
What is an operator?
--------------------

Operator is a language constructor that returns a value. For example we have
operators like add, subtract or compare.

Operators can use one or more arguments. For example the character * is a double
argument operator. On its left and right hand side there are values (here:
values that we want to divide). Another argument operator is the -. We use it
for negative numbers(-5, -10.234, etc.). It is also a double argument opertor,
as it can be used for subtraction.

The values the operator acts on are called operands.

Here are the operators available in Python:

Arithmetic operators:   +, -, *, **, /, //, % Compare operators:      ==, !=, <,

>, <=, >= Assignment operators:   =, +=, -=, *=, **=, /=, //=, %=, &=, ^=, |=,

<<=, >>= Identity operators:     is, is not Logical operators:      and, or, not

Membership operators:   in, not in Bitwise operators:      & AND, | OR, ^ XOR, ~
NOT, << left shift, >> right shift


--------------------
Arithmetic Operators
--------------------

They are used for arithmetic operations - such as addition or subtraction etc.

# Mathematic operations
    >>> print(1 + 2 + 5 - (2 * 2))
    4
    >>> print(501.0 - 99.9999)
    401.0001
    >>> print(2 ** 3)
    8
    >>> print(10 / 4)
    2.5
    >>> print(10 // 4)
    2
    >>> print(5 % 2)
    1

    Operators in Python are sensitive to the sequence of actions. They use the
    same rules as in mathematics.   
"""

# words concatenation
name = "John"
greeting = "Hello, " + name
print(greeting) # Return "Hello, John"
adam = "Adam"
eva = "Eva"
print(adam + " and " + eva)

# words repeat
message = "Hey"
print(message * 2) # return HeyHey
new_message = "Hi" * 5
print(new_message)
number = 3
message = message * number
print(message)

"""
A few details:

^ is an exponentiation symbol

/ this is a sign of real division i.e. the result is always a real number with a
decimal value (even if it's a 0) 

// this is integer division i.e. the resultwill be an integer number. If the
operation is on non-integer numbers, the operator will cut off the decimal
without rounding it.

% this is the modulo operator, it returns the remainder of integer division

Python allows for the addition of strings (a.k.a. to concatenate, or join) or to
multiply them by some natural number (as a result we get a repeated string)

--------------------
Assignment Operators
--------------------
"""
num =3
num = num + 4
print(num) # num value 7
num += 2
print(num)
num -= 1
print(num) # prints 8
num = num * 3
print(num) # num value 24
num /= 2
print(num)
num **= 3
print(num) # returns 1728
num = num // 3 # integer division
print(num) # num value
num %= 5
print(num)

# -----------------
# Compare operators
# -----------------

john_1 = "John"
john_2 = "John"
print(john_1 == john_2)
print(1 != 1)
print(99 < 1.1)
print(99 > 1.1)
print(-32 >= -33)
print(123 <= 123)

# -----------------
# LOGICAL OPERATORS
# -----------------

print(True or False)
print(False and False and True)
print(not False)
is_greater = 40 > 30
print(not is_greater)

# ------------------
# IDENTITY OPERATORS
# ------------------

print("fox" not in "cow, dog, cat")
print("cool" in "Python is cool!")