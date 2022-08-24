import random

attempts = 6
attempts_const = attempts
numb_from = 1
numb_to = 50
number = random.randint(numb_from, numb_to)
tmp = ''

print(f'\033[38;2;201;100;58mPick a number between {numb_from} and {numb_to}.\033[0m You have \033[32m{attempts}\033[0m attempts.\nEnter your guess and press \"Enter\".')

while attempts > 0:
    try_number = int(input(f'{tmp}'))
    attempts -= 1
    if try_number < number:
        tmp = f'👍 Greater than {try_number}\n'
    if try_number > number:
        tmp = f'👎 Less than {try_number}\n'
    if try_number == number:
        print(f'\033[32mYou WON 😒 in {attempts_const - attempts} attempts')
        break
    if try_number != number and attempts == 0:
        print(f'\033[3;31mYou lost\033[0m 🤡 \033[3;31mThe number is - {number}')
        break