"""
OBJECTS are represented by attributes (as variables) and methods (functions
defined for object and called on object), which can read and modify an
object attribute.

CLASSES provide a blueprint for how an object should be defined. They are
used to create new user-defined data structures.

OBJECTS are instances of CLASSES.
"""
# class Student:
#     def __init__(self):
#         self.name = "John"
#         self.grade = 4
#
#
# class Animal:
#     SPECIES = ""
#
#     def __init__(self):
#         self.name = "Johny"
#         self.age = 2
#
#     def print_details(self):
#         print(f'Name: {self.name}, age: {self.age}')

"""
Instantiating Objects
---------------------
"""

# snoopy = Animal()
# my_dog = Animal()
# my_dog.print_details()
#
# print(my_dog.name)
# my_dog.age = 3
# my_dog.print_details()
#
# puppy = Animal()
# dog = Animal()
# puppy.age = 1
# puppy.name = "Rex Junior"
# dog.age = 10
# dog.name = "Rex Senior"
#
# print(f'My dog: {puppy.name}, {puppy.age} and older dog: {dog.name}, '
#       f'{dog.age}')

"""
---------------------
Initializer __init__
---------------------
"""

# class Animal:
#     def __init__(self, name="Rex", age=2):
#         self.name = name
#         self.age = age
#
# my_cat = Animal("Snoopy", 5)
# my_parrot = Animal("Ara")
# my_turtle = Animal()
# print(my_parrot.age)
# print(my_turtle.name)

"""
---------------------
Basic Magic Methods
---------------------

The ones that begin and end with a double floor, underscore.
__init__ is an example of such a function.

Magic classes ensure that Python enters smoothly into the Python ecosystem, 
i.e. be comparable, sortable or, for example, be able to cope if we pass 
them functions such as len or str.
"""
# __str__ and __repr__

# class Animal:
#     def __init__(self, name="Rex", age=2):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"<{self.name} ({self.age})>"
#
# print(Animal())

"""
The handling of __repr__function is similar. The main difference between 
them is the purpose. __str__ is used when creating the human representation 
of an object and __repr__ is used when creating an object representation for 
the computer.

COMPARISON OPERATORS
----------------------

The set of comparison operators and their corresponding magic methods:

<  and corresponding method: __lt__
<= and corresponding method: __le__
== and corresponding method: __eq__
!= and corresponding method: __ne__
>= and corresponding method: __ge__
>  and corresponding method: __gt__
"""

# class Animal:
#     def __init__(self, name="Rex", age=2):
#         self.name = name
#         self.age = age
#
#     def __gt__(self, other):
#         return self.age > other.age
#
#     def __len__(self):
#         return self.age
#
# print(Animal('Alex', 3) > Animal('Milk', 2))

"""
-------------------------------------------------
Mathematical Operators and Casting to Other Types
-------------------------------------------------
"""

# __add__      operator: +
# __sub__      operator: -
# __mul__      operator: *
# __floordiv__ operator: //
# __truediv__  operator: /
# __mod__      operator: %
# __pow__      operator: **
# __lshift__   operator: <<
# __rshift__   operator: >>
# __and__      operator: &
# __xor__      operator: ^
# __or__       operator: |

"""
We can also teach our classes to be projected to, for example, and int. The 
following methods are used for this:

int()   __int__
long()  __long__
float() __float__
oct()   __oct__
hex()   __hex__
"""

# class Animal:
#     def __init__(self, name="Rex", age=2):
#         self.name = name
#         self.age = age
#
#     def __add__(self, other):
#         return Animal(self.name, self.age + int(other))
#
#     def __str__(self):
#         return f"<{self.name} ({self.age})>"
#
#     def __int__(self):
#         return self.age
#
# print(Animal("Alex", 1) + 1)
#
# print(Animal("Alex", 3) + Animal("Milk", 2))

"""
----------------------------
Private and Public Variables
----------------------------

# protected variable
--------------------
 self._name = name
 
 This is a suggestion to other programmers that a variable can only be 
 modified by a method of this class. Only a suggestion!
"""

# class Animal:
#     def __init__(self, name="Rex", age=2):
#         self._name = name
#         self._age = age
#
# my_dog = Animal()
# print(my_dog._name)

# ----------------
# private variable
# ----------------

# To set real variable privacy, you need to add __ to the variable name:
# __name or __age
# In this case, the variable value set will not be possible without class
# method usage - otherwise, Python will return an error AttributeError (it's
# treated as such attribute does not exist, it's hidden). Such variables are
# called private.

# class Animal:
#     def __init__(self, name='Rex', age=2):
#         self.__name = name
#         self.__age = age
#
# my_dog = Animal()
# print(my_dog.__name) # results in an error

"""
---------------------------------
Changing a private variable value
---------------------------------
"""
# class Animal:
#     def __init__(self, name="Rex", age=2):
#         self.__name = name
#         self.__age = age
#
#     def set_age(self, age):
#         if age > 0:
#             self.__age = age
#         else:
#             print("Age must be greater than 0.")
#
#     def get_age(self):
#         return self.__age
#
# my_dog = Animal()
# my_dog.set_age(3)
# print(my_dog.get_age())

"""
----------
Properties
----------

In the example above we prevent the user from cheating and we set a negative
number for the age. In order to do so use a separated method to show the 
attribute and another method to set it.
Instead of methods like set_age or get_age, we can use the method property (
with a specific attribute), that helps encapsulate variables in a python 
way. It's safer attribute management without additional method definition.
- property might have methods getter, setter and deleter;
- the name of the method that uses a property mechanism for setting 
operations i.e. set and delete needs to be the same!
"""
# class Animal:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     @property # getter - get variable value
#     def age(self):
#         return self.__age
#
#     @age.setter # setter - set variable new value
#     def age(self, age):
#         if age > 0:
#             self.__age = age
#         else:
#             print('Age must be greater than 0.')
#
#     @age.deleter # deleter - remove variable
#     def age(self):
#         del self.__age

"""
-------------------
Value and Reference
-------------------

When we assign an object to a variable, we create the relation called 
REFERENCE. If many variables are related to the same object, we can modify 
it by using any of them. The user can change the object state using one 
variable, and it will be propagated in other variables which are set to this 
object. This way we can use objects as function arguments, other objects 
methods or move between files and still we will use the same instance, 
with the same values and methods.
"""

# class Animal:
#     def __init__(self, name='Rex', age=2):
#         self.name = name
#         self.age = age
#
# dog_a = Animal()
# dog_b = dog_a
# print(f'Dog A name: {dog_a.name}')
# print(f'Dog B name: {dog_b.name}')
#
# dog_a.name = "Pongo"
# print(f'Dog A name: {dog_a.name}')
# print(f'Dog B name: {dog_b.name}')

"""
-------------------------------------
OBJECT-ORIENTED PROGRAMMING PARADIGMS
-------------------------------------

------------
ABSTRACTION
------------

Abstraction is an idea that is not related to a specific instance. It's 
difficult to imagine an idea of an animal or a fruit. We will instinctively
think about some specific, existing object: a dog, a cat, an apple or a 
banana. In this case we don't want to get a specific type of animal or a 
fruit, but only that abstract concept that is not imaginable.

For object-oriented programming the class is often defined, instead of the 
implementation. This way we can create a basis that we can extend.

-------------
ENCAPSULATION
-------------

Encapsulation is a mechanism to hide data implementation by a limit visible 
only to public methods. Instance variables are defined as private and access
methods are public - they are used to update private variable values. This 
is called encapsulation.

Python is a specific language, because it offers huge freedom - it can be 
used without an explicit property or it can incorprate private variables. By
default variable values are used - variables and methods are available from 
each module or from other class objects etc.

------------
INHERITANCE
------------

Inheritance allows the child class to use methods and attributes from the 
base (parent) class. The child class automatically gets access to the same 
variables and methods as in the parrent class. This way we save time. Also 
when we want to create a class which is similar to another, we don't need to 
re-write or copy the same code - we just need to inherit the older class.

Inheritance expresses the relationship <<is>>. For example, a dog is an 
animal, a banana is a fruit. Based on this relation, the class Banana looks 
like a perfect candidate to get the Fruit class functionality.
"""

# class Human:
#     def __init__(self, name, height, weight):
#         self.name = name
#         self.height = height
#         self.weight = weight
#
# class Programmer(Human):
#     def __init__(self, name, height, weight, languages):
#         super().__init__(name, height, weight)
#         self.languages = languages
#
# bob = Programmer('Bob', 180, 100, ['Python', 'Java'])
# print(bob.name)

"""
------------
POLYMORPHISM
------------

Polimorphism is synonymous with "various". It means one name/object/method 
has many ways of usage. We use it by overwritting methods. A child class 
inherits methods from its parent, it can re-define them and use it to its 
liking. Polymorphism is strongly related to inheritance. We can create code,
that will work in the parent class (over type) and it will work in every 
child class (under type). Both the child and the parent class will have 
access to the same methods.
"""

class A:
    def __init__(self):
        pass

    def print_value(self):
        print('some value')


class B:
    def __init__(self):
        pass

    def print_value(self):
        print('other value')