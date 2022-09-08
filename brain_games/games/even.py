"""Module for checking the even logic."""
import random

import prompt


def welcome_user():
    """Ask for a name of user.

    :return: name
    """
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=name))
    return name


def random_number():
    """Randomize a number.

    :return: random number
    """
    return random.randint(0, 100)


def wrong_answer(answer, name):
    """
    Wrong answer of user logic.

    :param: answer, name
    """
    text = 'is wrong answer ;(. Correct answer was'
    if answer == 'yes':
        print("'{answer}' {message} 'no'.Let's try again, {name}!".format(
            answer=answer, name=name, message=text,
        ),
        )
    elif answer == 'no':
        print("'{answer}' {message} 'yes'.\nLet's try again, {name}!".format(
            answer=answer, name=name, message=text,
        ),
        )
    else:
        print(
            "'{answer}' is wrong answer ;(\nLet's try again, {name}!".format(
                answer=answer, name=name,
            ),
        )


def user_answer():
    """
    Answer from user.

    :return: answer
    """
    return prompt.string('Your answer: ')


def even_checking(name):
    """Check entered number - even or not."""
    count = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while count != 3:
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
            return wrong_answer(answer, name)

    print('Congratulations, {name}!'.format(name=name))
