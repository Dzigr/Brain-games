"""Module for arithmetic progression."""
from random import randint

GAME_RULE = 'What number is missing in the progression?'


def generate_round(max_step=15):
    """Check for right missing number in the random progression.

    One of the number under the random index replaced for dots.

    :return: right answer, question
    """
    start = randint(1, 100)
    step = randint(3, max_step)
    progression = [num for num in range(
        start,
        start + step * randint(6, 10),
        step,
    )]
    dots = randint(1, len(progression) - 1)
    right_answer = progression[dots]
    progression[dots] = '..'
    question = '{progression}'.format(
        progression=' '.join(map(str, progression)))
    return right_answer, question
