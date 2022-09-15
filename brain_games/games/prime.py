"""Module for prime numbers."""
from random import randint

GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_core():
    """Check for prime number.

    :return: right answer
    """
    number = randint(1, 100)
    print('Question: {requested_number}'.format(requested_number=number))
    prime_list = [
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
    ]
    return 'yes' if number in prime_list else 'no'
