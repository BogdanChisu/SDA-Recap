"""
------------------
PYTHON INTERPRETER
------------------

When the:

python <program_name.py>

command is run, a process is started to perform a series of steps that
ultimately lead to the interpretation of the code.

1. Sequential processing of code from a file, instruction by instruction -
the lines are read in a similar way as a human would do it: from top to bottom.
2. Compilation of source code into the so-called bytecode
3. Reading bytecode on a Python virtual machine
4. Code Execution

THE INTERPRETER translates our human-readable code into a series of numbers
and memory addresses that must be referred to in order to properly
understand and interpret the series of numbers. This generated code is
called BYTECODE. The next step is to use the translated data string to start
the program by using the PYTHON VIRTUAL MACHINE (PVM). Thanks to this
scenario, Python is independent of the environment and hardware on which the
programs written in that language are run. There is an additional third
instance between the processor that actually executes the instructions and
the code: the interpreter, which as a separate, special program is
responsible for the code execution model.

----------------------
PYTHON VIRTUAL MACHINE
----------------------

The Python Virtual Machine (PVM) is a Python runtime engine. It's a cycle
that iterates over bytecode instructions to run one by one.
PVM is not an isolated Python component. It is only a part of the system
installed on the computer. The Python Virtual Machine is the last element in
the *software* called the interpreter.

---------
FILES pyc
---------

The interpreter, reading the .py modules - files that are imported into
others in the application, converts the listing contained in them to
bytecode. At the same time, it creates special .pyc files with the same name as
the interpreted module, but with a different extension. They are the storage
location for the bytecode. It remains intact, and when the application is
restarted, the step of interpreting these files will be skipped, thanks to
which everything will be done a little faster. This can be compared to
searching the phone book several times: the second time, instead of starting
the search again, we will move to the page marked by the tab, so we save
some time. The .pyc file will change (it will be re-arranged by the
interpreter) if and only if the source code of the corresponding .py file
changes. Files with the extension .pyc are stored in the folder __pycache__.

-------------
INTERPRETERS
-------------

Python is just a syntax specification. When people talk about Python,
they often mean not only the language but also the implementation of
CPython. There are many different implementations that support this
specification.

-------
CPython
-------

The most popular and default implementation of Python is called CPython and
was written in C (hence the name). CPython provides the highest level of
compatibility with Python packagesand C language extension modules. There
are librariels that allow to use the code implemented in C and vice versa.

-----
PyPy
-----

PyPy is a Python implementation written in Python. PyPy strives for maximum
compatibility with the reference implementation of CPython, while improving
performance. If you want to improve the performance of your Python code,
try PyPy. Many numerical operations are often faster than those performed in
CPython. In the test suite it is currently over 5 times faster than CPython.
What's more, all standard libraries are written in pure Python, so you don't
need to know C to read them.

------
Jython
------

Jython is a Python interpreter written in Java. It compiles Python code into
Java bytecode (!), which is executed by the Java Virtual Machine, JVM) -
something like a virtual machine in Python. By using it, we get the
opportunity to use Java libraries.

Jython currently supports versions up to Python 2.7.

-----------
IronPython
-----------

IronPython is a Python interpreter written in C#. It can use both Python and
.NET libraries, and can also share Python code with other languages in .NET.

Same as Jython, it doesn't support Python 3. implementation.

--------------------
Modules and Packages
--------------------

Python, in addition to importing functions from embedded libraries, allows
for the use of the same mechanisms when incorporating code from the modules...

# IMPORTING MODULES
# -----------------

Consider an example where we have five files in the current directory:

current_dir:
    |_ modul_a.py
    |_ modul_b.py
    |_ modul_c.py
    |_ modul_d.py
    |_ modul_e.py

The file modul_a.py  is the module which stores the definition of the
function named find_index and the variable named test. It also does not
belong in the standard Python library. Other modules might get objects
defined in modul_a.py to prevent code duplication. If any module needs the
functionality offered by find_index, it could either write its own function
or use an existing one. The second option is preferable: it shortens the
amount of code and, in the event of an error, you make changes in only one
block instead of five, which significantly reduces the working time and
prevents the generation of subsequent errors.

Below you will find modul_a.py:
"""

# test = "Some description"
#
# def find_index(to_search, target):
#     for index, value in enumerate(to_search):
#         if value == target:
#             return index
#     return -1

"""
The find_index function returns the index of the target element if it 
appears on the to_search list if it is not found.

You can import author files in four ways similar to how importing code is 
done from embedded libraries.


--------------
THE 1st METHOD
--------------

After executing the code from the file modul_b.py, the string 'Some string' 
should be printed correctly and the value 0 should be displayed, because the 
string 'Gym' is just under such an index in the list courses.

modul_b.py
----------
"""

# Import module
# import modul_a
#
# print(modul_a.test)
# courses = ['Gym', 'History', 'Mathematic']
# index = modul_a.find_index(courses, 'Gym')
# print(index) # Return 0

"""
In this example, the entire module module_a.py has been imported, so use the 
dot operator to get to the sourced objects...
"""

"""
---------------
THE 2nd METHOD
---------------

The module modul_c.py works exactly like the previous one. It only differs 
in the way it imports external dependencies.
"""
# modul_c.py
# import modul_a as m_a
#
# print(modul_a.test)
# courses = ['Gym', 'History', 'Mathematic']
# index = m_a.find_index(courses, 'Gym')
# print(index) # Return 0

"""
If the module name is considered to be too long to be preceded by a call to 
each function, you can shorten that name in the middle of the modul_c.py 
file. You can do that by calling it using the command import modul_a as m_a. 
From now on in the modul_c.py file, all components of the imported module 
should be referred to by name m_a, because it became a local alias (
nickname) of the name modul_c. The previous name can no longer be used.

---------------
The 3rd METHOD
---------------

Below you will find the modul_d.py which showcases how to handle code insource:
"""

# modul_d.py

# Import only the find_index function

# from modul_a import test, find_index
#
# courses = ['Gym', 'History', 'Mathematic']
# index = find_index(courses, 'Gym')
# print(index) # Return 0

"""
There is no need to import the entire file - only its selected components. 
If instead of the entire modul_a we import only the function find_index we 
lose access to the variable test, also declared by the module. By importing 
the whole module, we will not have to precede the function name find_index 
with the module name or use the dot operator. If it is also necessary to use
the variable test, it can be attached to the module by using a comma.

--------------
The 4th METHOD
--------------

Importing all attributes of a given modules is possible thanks to the 
asterisk operatorIt should be remembered that this is not a recommended 
practice and may cause problems if a name collision occurs in our file or 
other module that we import in a similar way.
"""
# modul_e.py
# Import all variables and functions

# from modul_a import *
#
# print(test)
# courses = ['Gym', 'History', 'Mathematic']
# index = find_index(courses, 'Gym')
# print(index) # return 0

"""
---------------------------------
HOW PYTHON SEARCHES FOR MODULES?
---------------------------------

All previous examples were based on the scenario where all modules are in 
the same directory. What would happen if the files were in other folders? 
Python looks for modules in the locations specified by the path list from 
the sys built-in library. The list of paths that will be searched to find 
imported modules can be obtained from this variable.

Here is the order of places Python looks in for a file which content we 
decided to include in the module:

1. The current directory
2. The elements derived from the system variable PYTHONPATH
3. The location of standard Python libraries
4. The location of additional external Python libraries (not included in the 
   installer)
   
When the locations in the sys.path list will not return any result and the 
module is not found, an ModuleNotFoundError exception will be returned.

sys.path list update
--------------------

Since the sys.path list is a list of locations to be searched, a new entry 
can be added dyna,ically while the program is running. This is not the best 
solution - the next step would be to add a new location at the top of each(
!) file that would use the imported module.

We can add a new location to the system variable  PYTHONPATH.
PYTHONPATH is a variable that tells Python where to look for additionan 
modules. The way you set system variable depende on the operating system - 
it is done differently under Linux and/or Windows. In Windows, this can 
easily be done through the user interface or using the set command in the 
command line. Linux programmers will need to use the export program.

An easy way to display the sys.path list:
"""
import sys

print(sys.path)

"""
------------------
ATTRIBUTE __file__
------------------

Each module has a special attribute __file__, which specifies the path to 
its location on the disk. We can write the value of this attribute in the 
console and open the file from the path indicated in the editor. The 
standard library modules are of course common Python files, so you can read 
them without any problems and you can learn a lot from them.
"""

import random

print(random.__file__)

"""
---------
PACKAGES
---------

Python packages are directories containing files with the extension.py.

For Python to take a directory as a package, it must contain a special file 
called __init__.py may be empty or it might contain generic code for the 
package. Its most important function is to be a Python marker so that it 
interprets the directory as a package.

- Importing entire packages
---------------------------

# Path to the school package must be
# added to the variable PYTHONPATH

import school
from school import student
from school import student, teacher
from school import *
from school import classroom as room 

- IMPORT CONVENTION
-------------------

1. One import per line - do not import modules after the comma!
2. It is forbidden to import classes, variables, etc. - only whole modules.
3. Imports must be divided into three sections:
    - modules from the standard library
    - modules from external libraries
    - modules inside the project (our code)
4. Within one section, imports should be listed alphabetically


----------------------------
TYPES OF LIBRARIES IN PYTHON
----------------------------

As already mentioned, libraries are divided according to the source they 
come from:
- internal - available after installing Python
- external - require downloading

Built-in libraries:
- os
- path
- math
- random

External libraries:
 - flask - A light framework for creating applications and websites.
 - django - A high level platform for creating web applications.
 - tensorflow - Google framework for creating machine learning models
 - ipython - an interactive shell with several amenities that are not found 
   in a regular terminal
   
   
----------------------------
Package Installer in Python
----------------------------

pip is a package manager that allows you to manage and include packages that
are not part of the standard Python library. It contains a large number of 
commands that should be used to manage external libraries.

Since Python version 3.4, pip is included in the installation package, 
making it an extremely important tool for this language programmer.

pip help - shows a list of basic commands
pip search <package_name>
pip install <package_name>
pip uninstall <package_name>
pip freeze
pip list -o
pip install -U <package_name> # update the selected package
pip install <package_name>==version
pip install <package_name>!=version
pip install <package_name>>=version
pip install <package_name>>=version_min, <version_max

-------------------------------
External Libraries in Projects
-------------------------------

Advanced projects can have a huge number of additional packages (up to 
several dozen per project. It's hard to imagine running the pip install 
command 50 times before we can start to program.

requirements.txt
----------------

pip freeze > requirements.txt

requirements.txt - read
------------------------

pip install -r requirements.txt
"""