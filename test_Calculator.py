import pytest
from assertpy import assert_that
from Calculator import Calculator
from NegativeNumberException import NegativeNumberException


class TestCalculator:
    @pytest.fixture
    def calc(self):
        self.calc = Calculator()

    def test_should_return_zero_when_got_empty_string(self, calc):
        result = self.calc.add("")
        assert_that(result).is_equal_to(0)

    def test_should_return_number_when_given_number(self, calc):
        result = self.calc.add("1")
        assert_that(result).is_equal_to(1)

    def test_should_add_two_numbers_separated_with_comma(self, calc):
        result = self.calc.add("1,2")
        assert_that(result).is_equal_to(3)

    def test_should_add_more_numbers_separated_with_comma(self, calc):
        result = self.calc.add("1,2, 3, 4    , 5, 6,7,8,9,10")
        assert_that(result).is_equal_to(55)

    def test_should_add_three_numbers_separated_with_comma_or_new_line(self, calc):
        result = self.calc.add("1,2\n4")
        assert_that(result).is_equal_to(7)

    def test_should_raise_exception_when_negative_number_provided(self, calc):
        assert_that(self.calc.add).raises(NegativeNumberException).when_called_with("-1")
