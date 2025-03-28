from random import choice, randint

import prompt

RANGE_CALC_NUMBERS = (1, 15)
SIGNS = ('+', '-', '*')


def get_right_answer(number1, sign, number2) -> str:
    return str(eval(f'{number1} {sign} {number2}'))


def play_calc_game() -> tuple:
    sign = choice(SIGNS)
    number1 = randint(*RANGE_CALC_NUMBERS)
    number2 = randint(*RANGE_CALC_NUMBERS)
    print(f'Question: {number1} {sign} {number2}')
    answer = prompt.string('Your answer: ')
    expected_answer = get_right_answer(number1, sign, number2)
    return expected_answer, answer
