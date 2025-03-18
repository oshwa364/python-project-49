from brain_games.games.calc_game import calc_game
from brain_games.engine import run_game
from brain_games.constants import CALC_INSTRUCTION


def main():
    run_game(calc_game, CALC_INSTRUCTION)


if __name__ == '__main__':
    main()
