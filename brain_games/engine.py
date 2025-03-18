import prompt

from brain_games.constants import ROUNDS


def run_game(game, instruction):
    username = prompt.string('Welcome to the Brain Games!\n'
                         'May I have your name? ')
    print(f'Hello, {username}!\n'
          f'{instruction}')
    
    for _ in range(ROUNDS):
        expected_answer, answer = game()
        if expected_answer != answer:
            print(f'\'{answer}\' is wrong answer ;(. '
                  f'Correct answer was \'{expected_answer}\'.\n'
                  f'Let\'s try again, {username}!')
            exit()
        print('Correct!')
    print(f'Congratulations, {username}!')
