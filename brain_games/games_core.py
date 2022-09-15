"""Module with common functions for all games."""
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


def general_core(game_module):
    """General core of all brain games.

    :param: game logic
    """
    user_name = welcome_user()
    print(game_module.GAME_RULE)
    for _ in range(ROUNDS):
        right_answer = game_module.game_core()
        user_answer = prompt.string('Your answer: ')
        if user_answer == str(right_answer):
            print('Correct!')
        else:
            wrong_answer(user_answer, user_name, right_answer)
            break
    else:
        print('Congratulations, {name}!'.format(name=user_name))


def wrong_answer(user_answer, user_name, right_answer):
    """
    Wrong answer of user logic.

    :param: user answer, name, right answer
    """
    text = """
    \r'{answer}' is wrong answer ;(. Correct answer was '{right_answer}'.
    \rLet's try again, {name}!
    """
    print(text.format(
        answer=user_answer,
        right_answer=right_answer,
        name=user_name,
    ),
    )
