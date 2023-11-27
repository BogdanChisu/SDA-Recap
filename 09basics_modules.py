"""
---------------------
Working With Modules
---------------------
Working with modules is better because:
- simplicity: by dividing the program into smaller elements, we focus on
smaller problems to be solved, which makes the software development process
simpler and generates fewer error
- easy to maintain: if each modules focuses on one task and is independent
of the other, the probability of impact on other parts of the program in the
case of modifications is reduced
- multiple use - functionality defined in one module can be imported into
another module and used in it without having to write the same functions or
use the "copy-paste" technique
- creating rages and namespaces - modules help to avoid collision of names
between identifiers in different parts of the program

-------------------
IMPORTING LIBRARIES
-------------------
"""

# Method 1
# -----------------
import math
# we import the entire content of the math module

result_fact= math.factorial(5)
print(result_fact)

result_sqrt = math.sqrt(16)
print(result_sqrt)

# Method 2
# ----------------

import math as m
# rename the module that you are importing to make it easier to use

result_fact = m.factorial(5)
print(result_fact)

result_sqrt = m.sqrt(16)
print(result_sqrt)

# Method 3
# --------------

from math import factorial
# import only the part of the module that you are going to use

result_fact = factorial(5)
print(result_fact)

from math import sqrt
result_sqrt = sqrt(16)
print(result_sqrt)

# Method 4
# -----------------

from math import *

result_fact = factorial(5)
print(result_fact)

result_sqrt = sqrt(16)
print(result_sqrt)

"""
-----------------------
The dir() function
-----------------------

With the dir() function you can find out what the python file we are 
currently working on has access to. As you can see, the amount of available 
material increases as the programs runs and the next lines of code are 
executed.

Variables whose name begin with '__' are python special variables. __name__ 
for example stores the name of the module that is currently being executed, 
and __builtins__ is the module that stores built-in functions.

-----------------------------
Examles of built-in libraries
-----------------------------

- axis: use the functionality of the operating system:
    -name of the system
    -access to environment variables
    -create or delete directories
    -navigate file trees

- sys: access to some variables used or maintained by the interpreter and 
functions of the interpreter. Exiting the Python application, tracking 
errors, capturing I/O errors

- random: a library that provides implementations of pseudo-random number 
generators. It allows ti generate numbers for given distributions - both int
and real numbers, mix data in collections, or choose randomly from a given 
pool.

- math: functions for rounding numbers, calculating the largest common 
divisor, powers, logarithms, trigonometric function etc.

- time: Provides various functions related to the calculation of elapsed time.

- logging: functions and classes that implement a flexible event logging 
system for applications and libraries

- tkinter: a standard library that provides the tools you need to create 
your own Python graphical interface

- unittest: Module that supports test automation, sharing configuration code 
and closing tests, aggregating tests into collections, and testing 
independence in reporting
"""
