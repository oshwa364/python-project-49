from random import choice, randint

import prompt

from brain_games.constants import SIGNS


def get_right_answer(number1, sign, number2) -> str:
    return str(eval(f'{number1} {sign} {number2}'))


def calc_game() -> tuple:
    sign = choice(SIGNS)
    number1 = randint(1, 25)
    number2 = randint(1, 10)
    print(f'Question: {number1} {sign} {number2}')
    answer = prompt.string('Your answer: ')
    expected_answer = get_right_answer(number1, sign, number2)
    return expected_answer, answer
