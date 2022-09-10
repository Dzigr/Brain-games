"""Module for arithmetic progression."""
from brain_games.games_core import (ROUNDS, arithmetic_progression,
                                    user_answer, welcome_user, wrong_answer)


def progression_checking():
    """Check for right missing number in progression.

    :return: user answer, name and right answer
    """
    name = welcome_user()
    count = 0
    print('What number is missing in the progression?')
    while count != ROUNDS:
        progression, right_answer = arithmetic_progression()
        print('Question: {progression}'.format(
            progression=' '.join(map(str, progression))),
        )
        answer = int(user_answer())
        if answer == right_answer:
            count += 1
            print('Correct!')
        else:
            return wrong_answer(answer, name, right_answer)
    print('Congratulations, {name}!'.format(name=name))
