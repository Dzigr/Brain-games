"""Module for checking the even logic."""
from random import randint

GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    """Check entered number - even or not.

    :return: right answer, question
    """
    number = randint(1, 100)
    right_answer = 'yes' if number % 2 == 0 else 'no'
    question = str(number)
    return right_answer, question
