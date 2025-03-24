#!/usr/bin/env python3

from brain_games.engine import run_game
from brain_games.games.progression_game import play_progression_game

PROGRESSION_INSTRUCTION = 'What number is missing in the progression?'


def main():
    run_game(play_progression_game, PROGRESSION_INSTRUCTION)


if __name__ == '__main__':
    main()
