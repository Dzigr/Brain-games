"""Module for calculation."""
import random

from brain_games.games_core import (ROUNDS, game_question, random_number,
                                    user_answer, welcome_user, wrong_answer)


def result_calculation():
    """Check the result with entered number by user."""
    name = welcome_user()
    count = 0
    print('What is the result of the expression?')
    while count != ROUNDS:
        right_answer = calculation()
        answer = int(user_answer())
        if answer == right_answer:
            count += 1
            print('Correct!')
        else:
            return wrong_answer(answer, name, right_answer)
    print('Congratulations, {name}!'.format(name=name))


def calculation():
    """Mathematics logic.

    To avoid big nums in expression the random number divide to 3.

    return: result of expression
    """
    math_operations = '*-+'
    first_num = round(random_number() / 3)
    second_num = round(random_number() / 3)
    question = '{first_number} {sign} {second_number}'.format(
        first_number=max(first_num, second_num),
        sign=random.choice(math_operations),
        second_number=min(first_num, second_num),
    )
    game_question(question)
    return eval(question)
