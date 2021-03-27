class Calculator:
    def add(self, _input):
        if not _input:
            return 0
        numbers = _input.split(",")
        numbers = [int(n) for n in numbers]
        return sum(numbers)
