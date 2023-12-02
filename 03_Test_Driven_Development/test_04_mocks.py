from unittest import TestCase
from unittest.mock import MagicMock, patch

import pytest

from test_03_mock import BlogPostHistory, AvgCalculator, Data


class BlogPostHistoryTests(TestCase):
    def test_change_title(self):
        mock = MagicMock()

        with patch('test_03_mock.BlogPostHistory.save', mock):
            post_history = BlogPostHistory('title', 'desc')
            post_history.change_title('title2')
            assert post_history.get_properties() == ('title2', 'desc')

    def test_change_desc(self):
        mock = MagicMock()

        with patch('test_03_mock.BlogPostHistory.save', mock):
            post_history = BlogPostHistory('title', 'desc')
            post_history.change_description('desc2')
            assert post_history.get_properties() == ('title', 'desc2')

    def test_problem_with_file(self):
        mock = MagicMock(side_effect=OSError)

        with patch('test_03_mock.BlogPostHistory.save', mock):
            post_history = BlogPostHistory('title', 'desc')
            with pytest.raises(Exception):
                post_history.change_description('desc2')


def test_calculate_avg():
    data = [['1', '2', '3', '4', '5'], ['2', '4', '1', '12']]
    mock = MagicMock(return_value=data)

    with patch('test_03_mock.AvgCalculator._get_content', mock):
        avg_calc = AvgCalculator('fake.txt')
        assert avg_calc.calculate() == [3.0, 4.75]

def test_get_raw_data():
    data = [['1', '2', '3', '4', '5'], ['2', '4', '1', '12']]
    mock = MagicMock(return_value=data)

    with patch('test_03_mock.AvgCalculator._get_content', mock):
        avg_calc = AvgCalculator('fake.txt')
        assert avg_calc.get_data() == data

"""
----------------
FIXTURE TESTING
----------------
"""

@pytest.fixture()
def prepared_object():
    data = Data()
    data.prepare("John", "Smith")
    yield data
    data.prepare("John", "Smith")

def test_first(prepared_object: Data):
    assert prepared_object.name == "John"
    prepared_object.prepare("John", "Test")
    assert prepared_object.info == "Test"

def test_second(prepared_object: Data):
    assert prepared_object.name == "John"
    prepared_object.prepare("Test", "Test")
    assert prepared_object.info == "Test"
    assert prepared_object.name == "Test"

# If we group the tests into a class it will look like this:

class Test(TestCase):

    def setUp(self):
        self.data = Data()
        self.data.prepare('John', 'Smith')

    def test_first(self):
        assert self.data.name == "John"
        self.data.prepare("John", "Test")

    def test_second(self):
        assert self.data.name == "John"
        self.data.prepare("Test", "Test")
        assert self.data.info == "Test"
        assert self.data.name == "Test"

    def tearDown(self):
        self.data.prepare("John", "Smith")