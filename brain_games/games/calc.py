"""Module for calculation."""
import operator
from random import choice, randint

GAME_RULE = 'What is the result of the expression?'


def generate_round():
    """Mathematics logic.

    return: right answer, question
    """
    operators = {'+': operator.add, '-': operator.sub, '*': operator.mul}
    sign = choice(list(operators.keys()))
    if sign == '*':
        first_num = randint(1, 10)
        second_num = randint(1, 10)
    else:
        first_num = randint(1, 100)
        second_num = randint(1, 100)
    question = '{first_number} {sign} {second_number}'.format(
        first_number=first_num,
        sign=sign,
        second_number=second_num,
    )
    return operators[sign](first_num, second_num), question
