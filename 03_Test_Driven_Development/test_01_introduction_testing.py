"""
-------------------------
WHY TESTING IS NECESSARY
-------------------------

1. Every body makes mistakes.

2. Not every case can be foreseen. Testing allows you to better understand
the system that is alive.

3. Advanced applications might have issues between components. Some elements
are mutually exclusive or their coexistence is impossible.

4. Correcting errors early in production is cheaper than reacting to
customer requests.

5. Testing provides information about system components and
facilitates understanding of component behavior.

6. Testing increases product quality

7. Avoid complications after merge requests. When working with git it may
happen that some code gets accidentally cut. Running the tests will inform
us immediately.

8. Refactor to make your code safer. Updating code to make it prettier is a
never-ending process. By refactoring we do not want to change the way the
system works. The tests help us make sure that the changes we have developed
have not changed the basic functionality.


-----------------------------
TDD (Test-Driven Development)
-----------------------------

TDD (Test-Driven Development) is a software development technique where we
first write tests for non-existent functionality and then we implement it.

TDD is not the only valid software development technique.

You can write tests in parallel with business logic or after implementing
code, but then it is no longer TDD. In Test-Driven Development, we always
write tests before implementation. TDD was originally part of extreme
programming. Now it is a standalone technique. It was created ny Kent Beck
(Creator of extreme programming and one of the creators of the Agile Software
Development Manifesto). An important point to remember - it is not a test
writing technique.


----------------
TDD Life Cycles
----------------

Writing and Running the test (the red phase)
--------------------------------------------

The first step is to write a test. At this point the test cannot be
successful because the functionality is not yet implemented. The code itself
might not compile. This may be the case if you wrote a test for a method
that does not exist yet.

Writing the Minimum Code to Pass the Test (the green phase)
-----------------------------------------------------------

In this phase we write the code responsible for the business logic. We need
to create the minimum amount of code. This way, when the test is run,
it goes into the "green" state. This means that the test has succesfully
passed. The important part is to create minimum code scope. We are not
trying to write the entire module. We are only interested in the code that
is under the scope of our test.

Code Refactoring (the refactor phase)
--------------------------------------

In this phase, we refactor the code so that it complies with all the
standards of good programming. This also applies to tests.

------------------
Advantages of TDD
------------------
    FOR THE DEVELOPER
    - higher comfort of work - it is also applicable to existing code,
    - documentation of high-level functionality,
    - better business and product knowledge,
    - greater chance of writting clean code,
    - easier start when working on a new project,
    - less pressure at work,

    FOR THE CLIENT
    - higher level of quality assurance for the application and fewer errors,
    - the ability to predict the cost of maintaining the application and
    including modifications to existing solutions,
    - fewer programmers need to be allocated to the project,
    - it is easier to locate and fix errors,
    - a greater understanding of the implemented solutions which can lead to
    improvment suggestions by the development team,
    - TDD leads to better code and a better application.

---------------------
DISADVANTAGES OF TDD
---------------------
    - the time and effort needed to train and prepare developers,
    - the need for discipline i.e. tests must be managed and improved over
    time in the same manner as all the other code,
    - initial investment of longer development time,
    - not all managers are convinced by the argument above. The total
    development time (including bug finding, fixing and code writing) is
    shorter in TDD than in non-TDD.


-----------
Test Levels
-----------

UNIT TESTS
----------

Unit tests are often called component tests or module tests. their main goal is
to find errors in the implementation of a given unit/component. The test
objects include: individual components in isolation, basic documentation,
the application design and other elements, i.e. requirements specification.
The word component can refer to a function, a class, and sometimes an entire
module.

    - unit testing is performed at a very low level of the application,
    It is very close to the source code of the software
    - These tests validate individual methods and functions of classes,
    components or modules used in the program.
    - Automating unit tests is generally quite cheap, and can be performed
    very quickly by the continuous integration server.

Integration tests
-----------------

The next level incorporates tests that check whether the components work
together correctly. One example is the cooperation between a web application
and a database. Another one - the link between two classes. Integration
testing is aimed at detecting errors during the interaction between systems
or its parts.
    - integration tests check whether the various modules or services used
    by the software work well together.
    - this level of integration can be used to check the interaction of the
    application with the database or to make sure that the micro-services
    work in accordance with the requirements and expectations.
    - this level of testing is more expensive than unit testing because it
    requires multiple application components to run.

System Tests
------------

We perform system tests when the system components have been integrated with
each other. This is the moment when we check the functionality of the
system. At this stage, we can run e2e (end to end) tests. End-to-end tests
are carried out from the user's point of view. They cover entire test
scenarios, e.g. from creating an account, through logging in to the system
and performing an operation to finally logging out. As a result we are able
to find out wether our system meets the original assumptions.
    - end-to-end testing simulates the behaviour of the full application
    environment.
    - This level of testing checks that all elements of the application work as
    intended.
    - Some of them can be extremely simple and rely on loading a website or
    logging in, while more complex scenarios include validation or e-mail
    notifications, online payments and many more scenarios

Acceptance Tests
----------------

Usually acceptance tests are performed on the client's side or by the end
users. For this type of task the tested application environment must be
fully operational. The main purpose of acceptance tests is not to find
errors, but make sure that the application meets the expectations of the
customer and it's users.
    - Acceptance testing is a formal software testing technique that is used to
     verify that a system meets business requirements.
     - It requires the entire application to be started and run properly in
     order to replicate user behavior.
     - These tests may also cover a slightly wider scope i.e. measuring of
     system performance and rejecting changes incase they do not achieve the
     requirements provided by the customer.


--------------------
Pytest - the basics
--------------------

What is PyTest?
---------------

PyTest is a modern framework for running automated tests in Python. It can
be used for unit tests. It also works very well for creating complex
higher-level tests for entire applications or libraries.

PyTest documentation
--------------------
https://docs.pytest.org/en/latest/contents.html

Why PyTest?
-----------

    - it allows to write small and easy tests
    - it has a multitude of plugins to make testing even easie
    - UnitTest can also be run there
    - we only have to use the word asser for comparison and we get very
    detailed information about the errors
    - we have dependency injection
    - we have the ability to create markers: pytest.mark.skipif or
    pytest.mark.xfail
    - we can parameterize tests, reducing the amount of code that is written
    - it automatically discovers test modules, classes, and functions - we
    do not have to use unnecessary class inheritance


# Installation
---------------
pip install pytest

# Run the pytest for a specific file
------------------------------------
pytest test_mymodule.py

# Run everything that has <special_run> in the name
---------------------------------------------------
pytest -k 'special_run'

# Run tests that are decorated with the selected marker_name
------------------------------------------------------------
pytest -m 'marker_name'


----------
FIRST TEST
----------
"""

# def add_numbers(a: int, b: int):
#     return a + b

"""
------------------
PyTest - examples
------------------
"""

# def sum_args(max_value, *args):
#     return 0

"""
    - we pass a number in max_value and all subsequent arguments are numbers 
    smaller than the max_value, we expect to find the sum of all numbers
    - we pass a number in max_value and not all subsequent arguments are 
    numbers less than max_value, we expect a sum of numbers to be less than or 
    equal to max_value
    - we pass a number in max_value and not all subsequent arguments are 
    numbers, they may be a string, we only expect the sum of numbers to be 
    smaller than the max_value
    - we pass a string in max_value and all subsequent arguments are 
    numbers, we only expect the sum of numbers to be less than or equal to 100 
    (the default value)
    - we pass a string in max_value and not all subsequent arguments are 
    numbers, we only expect the sum of numbers to be less than or equal to 100 
    (the default value)
    
After running and failing the tests, we can rewrite the <sum_args> function.
"""

# def sum_args(max_value, *args):
    # sum_of_elements = 0
    # for val in args:
    #     if val < max_value:
    #         sum_of_elements += val
    #
    # return sum_of_elements

# def sum_args(max_value, *args):
#     sum_of_elements = 0
#     for val in args:
#         if val < max_value and isinstance(val, int):
#             sum_of_elements += val
#
#     return sum_of_elements

# def sum_args(max_value, *args):
#     sum_of_elements = 0
#     max_value = 100 if not isinstance(max_value, int) else max_value
#     for val in args:
#         if isinstance(val, int) and val < max_value:
#             sum_of_elements += val
#
#     return sum_of_elements

# def capital_case(x):
#     return x.capitalize()

# def capital_case(x):
#     if not isinstance(x, str):
#         raise TypeError('Please provide a string argument')
#     return x.capitalize()

"""
---------------------
What is TestCoverage?
---------------------

Test Coverage shows how much of our code is tested. It also shows paths 
which are not tested.

Installation and Usage
----------------------

pip install coverage

Running the analysis:
---------------------

coverage run --source="." --omit="*/venv/*" -m pytest

Creating a report
-----------------

coverage report product.py company.py

the result is:

coverage report example.py
"""