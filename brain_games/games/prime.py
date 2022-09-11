"""Module for prime numbers."""
from brain_games.games_core import (ROUNDS, random_number, user_answer,
                                    welcome_user, wrong_answer)


def prime_comparing(number):
    """Compare number with the list of prime numbers.

    :param: number
    :return: yes or no
    """
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


def prime_checking():
    """Check for prime number.

    :return: user answer, name and right answer
    """
    name = welcome_user()
    count = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while count != ROUNDS:
        number = random_number()
        print('Question: {requested_number}'.format(requested_number=number))
        right_answer = prime_comparing(number)
        answer = user_answer()
        if answer == right_answer:
            count += 1
            print('Correct!')
        else:
            return wrong_answer(answer, name, right_answer)
    print('Congratulations, {name}!'.format(name=name))
