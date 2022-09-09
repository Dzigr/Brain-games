"""Module for greatest common divisor."""
from brain_games.games_core import (ROUNDS, random_number, user_answer,
                                    welcome_user, wrong_answer)


def divisor_checking():
    """Check for greater divisor between 2 nums.

    :return: user answer, name and right answer
    """
    name = welcome_user()
    count = 0
    print('Find the greatest common divisor of given numbers.')
    while count != ROUNDS:
        given_numbers = (random_number(), random_number())
        print('Question: {first_number} {second_number}'.format(
            first_number=given_numbers[0],
            second_number=given_numbers[1],
        ),
        )
        right_answer = divisor_calculation(sorted(given_numbers))
        answer = user_answer()
        if answer == right_answer:
            count += 1
            print('Correct!')
        else:
            return wrong_answer(answer, name, right_answer)
    print('Congratulations, {name}!'.format(name=name))


def divisor_calculation(numbers):
    """Mathematics logic.

    :return: greatest divisor
    """
    if numbers[1] % numbers[0] == 0:
        return numbers[0]
    else:
        for num in range(int(numbers[1] / 2), 0, -1):
            if (numbers[1] and numbers[0]) % num == 0:
                return num
