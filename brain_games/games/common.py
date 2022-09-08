"""Module for checking the even logic."""
import random

import prompt


def welcome_user():
    """Ask for a name of user.

    :return: name
    """
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=name))
    return name


def random_number():
    """Randomize a number.

    :return: random number
    """
    return random.randint(0, 100)


def wrong_answer(answer, name):
    """
    Wrong answer of user logic.

    :param: answer, name
    """
    text = """'{answer}' is wrong answer ;(. Correct answer was '{right_answer}'.
    \rLet's try again, {name}!
    """
    if answer == 'yes':
        print(text.format(answer=answer, right_answer='no', name=name))
    elif answer == 'no':
        print(text.format(answer=answer, right_answer='yes', name=name))
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
