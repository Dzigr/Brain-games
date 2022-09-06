"""Module for checking the even logic."""
import prompt
import random


def welcome_user():
    """Asking for a name of user."""
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=name))
    return name


def even_checking(name):
    """Checking entered number - even or not."""
    count = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while count != 3:
        random_number = random.randint(0, 100)
        print('Question: {}'.format(random_number))
        user_answer = prompt.string('Your answer: ')
        if random_number % 2 == 0 and user_answer == 'yes':
            count += 1
            print('Correct!')
        elif random_number % 2 == 1 and user_answer == 'no':
            count += 1
            print('Correct!')
        else:
            if user_answer == 'yes':
                return print("'{answer}' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!".format(answer=user_answer, name=name))
            elif user_answer == 'no':
                return print("'{answer}' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!".format(answer=user_answer, name=name))
            else:
                return print("'{answer}' is wrong answer ;(\nLet's try again, {name}!".format(
                    answer=user_answer, name=name))
    print('Congratulations, {name}!'.format(name=name))


