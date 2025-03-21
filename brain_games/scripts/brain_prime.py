#!/usr/bin/env python3

from brain_games.constants import PRIME_INSTRUCTION
from brain_games.engine import run_game
from brain_games.games.prime_game import play_prime_game


def main():
    run_game(play_prime_game, PRIME_INSTRUCTION)


if __name__ == '__main__':
    main()
