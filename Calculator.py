import re

from NegativeNumberException import NegativeNumberException


class Calculator:
    def __init__(self):
        self.negatives = ""

    def add(self, _input):
        if not _input:
            return 0
        self.negatives = "Negatives:"
        numbers = re.split(",|\n", _input)
        numbers = [int(n) if int(n) >= 0 else self.negative_number(n) for n in numbers]
        if self.negatives != "Negatives:":
            raise NegativeNumberException(self.negatives)
        return sum(numbers)

    def negative_number(self, number):
        self.negatives += " " + number
