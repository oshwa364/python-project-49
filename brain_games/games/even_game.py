from random import randint

import prompt


def is_even(number) -> bool:
    return True if number % 2 == 0 else False


def get_right_answer(number) -> str:
    return 'yes' if is_even(number) else 'no'


def even_game() -> tuple:
    number = randint(1, 100)
    print(f'Question: {number}')
    answer = prompt.string('Your answer: ')
    expected_answer = get_right_answer(number)
    return expected_answer, answer
