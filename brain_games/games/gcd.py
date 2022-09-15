"""Module for greatest common divisor."""
from random import randint

GAME_RULE = 'Find the greatest common divisor of given numbers.'


def game_core():
    """Check for greater divisor between 2 nums.

    :return: right answer
    """
    given_numbers = (randint(1, 100), randint(1, 100))
    print('Question: {first_number} {second_number}'.format(
        first_number=given_numbers[0],
        second_number=given_numbers[1],
    ),
    )
    for num in range(max(given_numbers), 0, -1):
        if modulo(given_numbers, num):
            return num


def modulo(numbers, num):
    """Check for modulo.

    :return: boolean
    """
    first_number, second_number = numbers
    if first_number % num == 0 and second_number % num == 0:
        return True
