"""
---------------
WHAT ARE MOCKS?
---------------

Mock is a replacement for an object that looks the same as a real object but we
are able to control its behavior i.e. define which values or functions it
should return.

Mocks capabilities:
-------------------
    - simulate a connection to a database,
    - simulate resources that are unavailable, e.g. connections to network
    services,
    - simulate objects that have not yet been created,
    - simulate an increase in the speed of tests;
"""

class BlogPostHistory:
    FILENAME = 'post.txt'
    SEPARATOR = ','

    def __init__(self, title, desc):
        self._title = title
        self._desc = desc

    def save(self):
        with open(self.FILENAME, 'a+') as f:
            data = f'{self._title}{self.SEPARATOR}{self._desc}'

            f.write(data)

    def change_title(self, title):
        self._title = title
        try:
            self.save()
        except OSError:
            raise Exception('BlogPost can\'t save history')

    def change_description(self, desc):
        self._desc = desc
        try:
            self.save()
        except OSError:
            raise Exception('BlogPost can\'t save history')

    def get_properties(self):
        return self._title, self._desc


class AvgCalculator:
    def __init__(self, filename):
        self.filename = filename

    def _get_content(self):
        with open(self.filename, 'r') as f:
            lines = f.readlines()
            return [line.split(',') for line in lines]

    def _ensure_casted_data(self):
        data = self._get_content()
        new_data = []
        for x in data:
            new_data.append([int(n) for n in x])

        return new_data

    def calculate(self):
        numbers = self._ensure_casted_data()
        return [sum(x) / len(x) for x in numbers]

    def get_data(self):
        return self._get_content()


"""
--------
FIXTURES
--------

Fixtures in PyTest represent a way to prepare data for tests and clean them up.
"""

import pytest

@pytest.fixture()
def my_fixture():
    print('I\'m the fixture setup')
    yield
    print('I\'m the fixture teardown')

def test_first(my_fixture):
    print("I'm the first test.")

"""
Its effect is:

I'm the fixture setup.

PASSED [100%]I'm the first test

I'm the fixture teardown

Which means that with the decorator @pytest.fixture, we mark the function 
that will be a fixture. The word yield separates the code that is used to 
prepare the environment for testing (setup) from the code that is used to 
clean up after the test (tearDown).

The applied fixtures for the test are simply passed in a parameter.

Suppose we have such a class:
"""

class Data:
    def __init__(self):
        self.name = None
        self.info = None

    def prepare(self, name, info):
        self.name = name
        self.info = info