"""Calculation script."""
# !/usr/bin/env python3
import brain_games.games.calc as core
from brain_games.games_core import launch_game


def main():
    """Greetings and checking the result of expression."""
    launch_game(core)


if __name__ == '__main__':
    main()
