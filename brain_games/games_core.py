"""Module with common functions for all games."""
import prompt

ROUNDS = 3


def launch_game(game_module):
    """General core of all brain games.

    :param: game logic
    """
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=user_name))
    print(game_module.GAME_RULE)
    for _ in range(ROUNDS):
        right_answer, question = game_module.generate_round()
        print('Question: {question}'.format(
            question=question,
        ),
        )
        user_answer = prompt.string('Your answer: ')
        if user_answer == str(right_answer):
            print('Correct!')
        else:
            print(
                "'{user_answer}' is wrong answer ;(. "
                "Correct answer was '{right_answer}'.".format(
                    user_answer=user_answer,
                    right_answer=right_answer,
                ),
            )
            print("Let's try again, {name}!".format(
                name=user_name,
            ),
            )
            break
    else:
        print('Congratulations, {name}!'.format(name=user_name))
