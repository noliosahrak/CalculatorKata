import re


class Calculator:
    def add(self, _input):
        if not _input:
            return 0
        numbers = re.split(",|\n", _input)
        numbers = [int(n) for n in numbers]
        return sum(numbers)
