"""Module for checking the even logic."""
import random

import prompt

ROUNDS = 3


def welcome_user():
    """Ask for a name of user.

    :return: name
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=name))
    return name


def random_number():
    """Randomize a number.

    :return: random number
    """
    return random.randint(1, 100)


def opposite_answer(answer):
    """Reverse answer.

    return: 'yes' or 'no'
    """
    if answer == 'yes':
        return 'no'
    return 'yes'


def wrong_answer(answer, name, right_answer):
    """
    Wrong answer of user logic.

    :param: answer, name
    """
    text = """'{answer}' is wrong answer ;(. Correct answer was '{right_answer}'.
    \rLet's try again, {name}!
    """
    if answer != right_answer:
        print(text.format(answer=answer, right_answer=right_answer, name=name))
    else:
        print(
            "'{answer}' is wrong answer ;(\nLet's try again, {name}!".format(
                answer=answer, name=name,
            ),
        )


def user_answer():
    """
    Answer from user.

    :return: answer
    """
    return prompt.string('Your answer: ')