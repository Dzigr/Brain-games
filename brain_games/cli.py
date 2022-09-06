"""Request for a name of user."""
import prompt


def welcome_user():
    """Asking for a name of user."""
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=name))
