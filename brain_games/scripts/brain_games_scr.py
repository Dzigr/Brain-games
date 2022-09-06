"""Main module."""
# !/usr/bin/env python3
from brain_games.cli import welcome_user


def main():
    """Greetings and request the name of user."""
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
