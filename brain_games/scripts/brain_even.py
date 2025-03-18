#!/usr/bin/env python3

from brain_games.constants import EVEN_INSTRUCTION
from brain_games.engine import run_game
from brain_games.games.even_game import even_game


def main():
    run_game(even_game, EVEN_INSTRUCTION)


if __name__ == '__main__':
    main()
