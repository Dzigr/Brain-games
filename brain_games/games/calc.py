"""Module for calculation."""
from brain_games.games_core import (random_number, user_answer, welcome_user,
                                    wrong_answer)
import random


def result_calculation():
    """Checking the result of expression match with entered number."""
    name = welcome_user()
    count = 0
    math_operations = "*-+"
    print('What is the result of the expression?')
    while count != 3:
        first_num = random_number()
        second_num = random_number()
        operation = random.choice(math_operations)
        question = 'Question: {first_number}{sign}{second_number}'.format(
            first_number=max(first_num, second_num), sign=operation,
            second_number=min(first_num, second_num),
        )
        right_answer = eval(question)
        answer = user_answer()
        if answer == right_answer:
            count += 1
            print('Correct!')
        else:
            return wrong_answer(answer, name, right_answer)
    print('Congratulations, {name}!'.format(name=name))



