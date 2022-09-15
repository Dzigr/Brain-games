"""Module for checking the even logic."""
from random import randint

GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_core():
    """Check entered number - even or not.

    :return: right answer
    """
    number = randint(1, 100)
    print('Question: {random_number}'.format(random_number=number))
    if number % 2 == 0:
        return 'yes'
    elif number % 2 == 1:
        return 'no'
