"""Module for checking the even logic."""
from brain_games.games_core import (ROUNDS, opposite_answer, random_number,
                                    user_answer, welcome_user, wrong_answer)


def even_checking():
    """Check entered number - even or not.

    :return: user answer, name and right answer
    """
    name = welcome_user()
    count = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while count != ROUNDS:
        number = random_number()
        print('Question: {random_number}'.format(random_number=number))
        answer = user_answer()
        if number % 2 == 0 and answer == 'yes':
            count += 1
            print('Correct!')
        elif number % 2 == 1 and answer == 'no':
            count += 1
            print('Correct!')
        else:
            return wrong_answer(answer, name, opposite_answer(answer))
    print('Congratulations, {name}!'.format(name=name))
