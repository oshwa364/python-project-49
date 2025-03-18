from brain_games.games.even_game import *
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    even_game(name)

if __name__ == '__main__':
    main()