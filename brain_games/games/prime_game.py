from random import randint

import prompt

RANGE_PRIME_NUMBERS = (3, 100)


def is_prime(number) -> bool:
    for i in range(2, number // 2):
        if number % i == 0:
            return False
    return True


def get_right_answer(number) -> str:
    return 'yes' if is_prime(number) else 'no'


def play_prime_game():
    number = randint(*RANGE_PRIME_NUMBERS)
    print(f'Question: {number}')
    answer = prompt.string('Your answer: ')
    expected_answer = get_right_answer(number)
    return expected_answer, answer
