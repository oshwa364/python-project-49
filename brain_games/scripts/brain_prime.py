#!/usr/bin/env python3

from brain_games.engine import run_game
from brain_games.games.prime_game import play_prime_game

PRIME_INSTRUCTION = 'Answer "yes" if given number is prime. ' \
                    'Otherwise answer "no".'


def main():
    run_game(play_prime_game, PRIME_INSTRUCTION)


if __name__ == '__main__':
    main()
