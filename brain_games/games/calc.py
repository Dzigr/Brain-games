"""Module for calculation."""
from random import choice, randint

GAME_RULE = 'What is the result of the expression?'


def game_core():
    """Mathematics logic.

    return: right answer
    """
    math_operations = choice('*-+')
    if math_operations == '*':
        first_num = randint(1, 10)
        second_num = randint(1, 10)
    else:
        first_num = randint(1, 100)
        second_num = randint(1, 100)
    question = '{first_number} {sign} {second_number}'.format(
        first_number=max(first_num, second_num),
        sign=math_operations,
        second_number=min(first_num, second_num),
    )
    print('Question: {question}'.format(
        question=question,
    ),
    )
    return eval(question)
