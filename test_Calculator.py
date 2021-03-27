import pytest
from assertpy import assert_that
from Calculator import Calculator


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
