import prompt
from random import randint
from math import gcd


def get_right_answer(number1, number2) -> str:
    return str(gcd(number1, number2))


def gcd_game() -> tuple:
    number1 = randint(1, 40)
    number2 = randint(1, 40)
    print(f'Question: {number1} {number2}')
    answer = prompt.string('Your answer: ')
    expected_answer = get_right_answer(number1, number2)
    return expected_answer, answer
