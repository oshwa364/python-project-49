from random import randint

import prompt


def is_prime(number) -> bool:
    for i in range(2, number // 2):
        if number % i == 0:
            return False
    return True


def get_right_answer(number) -> str:
    return 'yes' if is_prime(number) else 'no'


def prime_game():
    number = randint(1, 100)
    print(f'Question: {number}')
    answer = prompt.string('Your answer: ')
    expected_answer = get_right_answer(number)
    return expected_answer, answer