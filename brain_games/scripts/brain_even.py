"""Even script."""
# !/usr/bin/env python3
import brain_games.games.even as core
from brain_games.games_core import general_core


def main():
    """Greetings and checking the number for even or not."""
    general_core(core)


if __name__ == '__main__':
    main()
