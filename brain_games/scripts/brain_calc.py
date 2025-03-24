#!/usr/bin/env python3

from brain_games.engine import run_game
from brain_games.games.calc_game import play_calc_game

CALC_INSTRUCTION = 'What is the result of the expression?'


def main():
    run_game(play_calc_game, CALC_INSTRUCTION)


if __name__ == '__main__':
    main()
