from random import randint


def is_even(number):
    return True if number % 2 == 0 else False


def expected_answer(number):
    return 'yes' if is_even(number) else 'no'


def round():
    number = randint(1, 100)
    print(f'Question: {number}')
    answer = input('Your answer: ')
    return True if expected_answer(number) == answer else False


def even_game(name):
    rounds = 3
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < rounds:
        if not round():
            print(f'Let\'s try again, {name}!')
            exit()
        print('Correct!')
        count += 1
    print(f'Congratulations, {name}!')
