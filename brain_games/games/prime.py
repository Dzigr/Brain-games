"""Module for prime numbers."""
from random import randint

GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_round():
    """Check for prime number.

    :return: right answer, question
    """
    number = randint(1, 100)
    question = '{requested_number}'.format(requested_number=number)
    right_answer = 'yes' if is_prime(number) else 'no'
    return right_answer, question


def is_prime(number):
    """Boolean check for prime number.

    :return: True/False
    """
    if number == 1:
        return False
    divider = 2
    while divider**2 <= number:
        if number % divider == 0:
            return False
        divider += 1
    return True
