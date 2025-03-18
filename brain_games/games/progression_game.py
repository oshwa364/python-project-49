import prompt
from random import randint, choice
from brain_games.constants import LENGTH_OF_PROGRESSION


def progression_game() -> tuple:
    first_number = randint(1, 20)
    step_of_progression = randint(2, 15)

    progression = [first_number + i for i in range(0, LENGTH_OF_PROGRESSION * step_of_progression, step_of_progression)]
    index_of_missing_number = randint(0, LENGTH_OF_PROGRESSION - 1)
    missing_number = progression[index_of_missing_number]
    progression[index_of_missing_number] = '..'
    progression_string = ' '.join (str(i) for i in progression)
    print(f'Question: {progression_string}' )
    answer = prompt.string('Your answer: ')
    expected_answer = str(missing_number)
    return expected_answer, answer