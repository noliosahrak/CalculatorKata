import re

from NegativeNumberException import NegativeNumberException


def negative_number():
    raise NegativeNumberException


class Calculator:
    def add(self, _input):
        if not _input:
            return 0
        numbers = re.split(",|\n", _input)
        numbers = [int(n) if int(n) >= 0 else negative_number() for n in numbers]
        return sum(numbers)
