from assertpy import assert_that
from Calculator import Calculator


class TestCalculator:

    def test_should_return_zero_when_got_empty_string(self):
        calc = Calculator()
        result = calc.add("")
        assert_that(result).is_equal_to(0)
