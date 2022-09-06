"""Even script."""
# !/usr/bin/env python3
from brain_games.even import even_checking, welcome_user


def main():
    """Greetings and checking the number for even or not."""
    print('Welcome to the Brain Games!')
    even_checking(welcome_user())


if __name__ == '__main__':
    main()
