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
        right_answer = divisor_calculation(given_numbers)
        answer = int(user_answer())
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
    for num in range(max(numbers), 0, -1):
        if modulo(numbers, num):
            return num


def modulo(numbers, num):
    """Check for modulo.

    :return: boolean
    """
    first_number, second_number = numbers
    if first_number % num == 0 and second_number % num == 0:
        return True
