"""Even script."""
# !/usr/bin/env python3
import brain_games.games.even as core
from brain_games.games_core import launch_game


def main():
    """Greetings and checking the number for even or not."""
    launch_game(core)


if __name__ == '__main__':
    main()
