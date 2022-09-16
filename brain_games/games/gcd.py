"""Module for greatest common divisor."""
from random import randint

GAME_RULE = 'Find the greatest common divisor of given numbers.'


def generate_round():
    """Check for greater divisor between 2 nums.

    :return: right answer, question
    """
    given_numbers = (randint(1, 100), randint(1, 100))
    question = '{first_number} {second_number}'.format(
        first_number=given_numbers[0],
        second_number=given_numbers[1],
    )
    return gcd(*given_numbers), question


def gcd(number1, number2):
    """Calculate greater divisor between 2 nums.

    :return: greater divisor
    """
    while number1 != number2:
        if number1 > number2:
            number1 -= number2
        else:
            number2 -= number1
    return number1
