# from test_01_introduction_testing import add_numbers
# from test_01_introduction_testing import sum_args
from test_01_introduction_testing import capital_case
import pytest

# def test_add_numbers():
#     a = 4
#     b = 7
#     expected = 11
#
#     assert add_numbers(a, b) == expected
#
# def test_add_numbers_with_negative_values():
#     a = -20
#     b = 3
#     expected = -17
#
#     assert add_numbers(a, b) == expected

# def test_sum_of_elements_below_max_val():
#     max_value = 10
#     elements = [2, 4, 5, 3, 9, 1, 0, -2]
#
#     expected = 22
#
#     assert sum_args(max_value, *elements) == expected
#
# def test_sum_of_elements_above_max_val():
#     max_value = 8
#     elements = [2, 4, 5, 3, 9, 1, 0, -2]
#
#     expected = 13
#
#     assert sum_args(max_value, *elements) == expected
#
# def test_sum_of_elements_with_mixed_types():
#     max_value = 8
#     elements = [2, 4, 5, 3, 'test']
#
#     expected = 14
#
#     assert sum_args(max_value, *elements) == expected
#
# def test_of_sum_elements_with_invalid_max_val():
#     max_value = 'test'
#     elements = [2, 4, 5, 3]
#
#     expected = 14
#
#     assert sum_args(max_value, *elements) == expected
#
# def test_sum_of_elements_with_invalid_max_val_and_mixed_types():
#     max_value = 'test'
#     elements = [2, 4, 5, 3, 'test']
#
#     expected = 14
#
#     assert sum_args(max_value, *elements) == expected

def test_capital_case():
    assert capital_case('Software') == 'Software'

def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        capital_case(9)