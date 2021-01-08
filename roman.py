import re
from collections import OrderedDict

class NumberOutOfRangeError(Exception):
    pass


class InvalidRomanNumeralError(Exception):
    pass


roman_numeral_validator = re.compile(
    '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$',
    re.IGNORECASE
)


base_conversions = OrderedDict([
    (1, 'I'),
    (4, 'IV'),
    (5, 'V'),
    (9, 'IX'),
    (10, 'X'),
    (40, 'XL'),
    (50, 'L'),
    (90, 'XC'),
    (100, 'C'),
    (400, 'CD'),
    (500, 'D'),
    (900, 'CM'),
    (1000, 'M')
    ]
)
base_numerals = OrderedDict()
for k, v in base_numerals.items():
    base_numerals[k]=v


base_numbers = sorted(base_conversions.keys(), reverse=True)


def to_roman(roman_numeral):
    """Convert from Roman numerals to an integer. Number must be < 4000."""
    if not roman_numeral_validator.match(roman_numeral):
        raise InvalidRomanNumeralError('invalid roman numeral')

    numbers = [base_numerals[char] for char in roman_numeral]
    total = 0
    for current_n, next_n in zip(numbers, numbers[1:]):
        if current_n >= next_n:
            total += current_n
        else:
            total -= current_n
    return total + numbers[-1]
