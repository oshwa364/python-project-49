#!/usr/bin/env python3

from brain_games.constants import GCD_INSTRUCTION
from brain_games.engine import run_game
from brain_games.games.gcd_game import play_gcd_game


def main():
    run_game(play_gcd_game, GCD_INSTRUCTION)


if __name__ == '__main__':
    main()
