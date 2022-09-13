"""Module with common functions for all games."""
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


def game_question(number1, number2='', sign=''):
    """Print for question.

    :param:first and second number, operator if needed.
    """
    print('Question: {num1} {sign} {num2}'.format(
        num1=number1, sign=sign, num2=number2,
    ),
    )


def arithmetic_progression(max_step=15):
    """Random progression.

    One of the number under the random index replaced fo dots.

    :return: progression, right answer
    """
    start = random_number()
    step = random.randint(3, max_step)
    progression = [num for num in range(
        start,
        start + step * random.randint(6, 10),
        step
    )]
    dots = random.randint(1, len(progression) - 1)
    right_answer = progression[dots]
    progression[dots] = '..'
    return progression, right_answer


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
    print(text.format(answer=answer, right_answer=right_answer, name=name))


def user_answer():
    """
    Answer from user.

    :return: answer
    """
    return prompt.string('Your answer: ')
