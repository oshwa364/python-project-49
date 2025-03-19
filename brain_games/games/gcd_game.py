from math import gcd
from random import randint

import prompt

from brain_games.constants import RANGE_GCD


def get_right_answer(number1, number2) -> str:
    return str(gcd(number1, number2))


def play_gcd_game() -> tuple:
    number1 = randint(*RANGE_GCD)
    number2 = randint(*RANGE_GCD)
    print(f'Question: {number1} {number2}')
    answer = prompt.string('Your answer: ')
    expected_answer = get_right_answer(number1, number2)
    return expected_answer, answer
