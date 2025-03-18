#!/usr/bin/env python3

from brain_games.games.progression_game import progression_game
from brain_games.engine import run_game
from brain_games.constants import PROGRESSION_INSTRUCTION


def main():
    run_game(progression_game, PROGRESSION_INSTRUCTION)


if __name__ == '__main__':
    main()
