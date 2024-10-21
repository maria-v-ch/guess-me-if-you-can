# Guess Me If You Can
# A number guessing game with inspirational quotes

import json
import random
from datetime import datetime
import os

# Constants
MAX_ATTEMPTS = 10
MIN_NUMBER = 1
MAX_NUMBER = 15
LOG_FILE = 'log.txt'
MAX_LOG_SIZE = 1024 * 1024  # 1 MB

count = 0
threshold = MAX_ATTEMPTS
guesses_less_than_magic_number = []
guesses_more_than_magic_number = []
sayings_list = []
time_now = datetime.now()
magic_number = random.randint(1, 15)
guess = int


def print_random_saying():
    with open('sayings.json', 'r') as file:
        sayings_list = json.load(file)
    random_saying = random.choice(sayings_list)
    print(f'{random_saying}')


def confirm_magic_number_is_more_than_guess(guess, magic_number):
    if guess != magic_number and magic_number > guess:
        print(f'Wrong guess, try again.')
        print_random_saying()
        print(f'You have {threshold - count} attempts left and the guessed number is actually more than {guess}.')
        guesses_less_than_magic_number.append(guess)
        return True
    return False


def confirm_magic_number_is_less_than_guess(guess, magic_number):
    if guess != magic_number and magic_number < guess:
        print(f'Wrong guess, try again.')
        print_random_saying()
        print(f'You have {threshold - count} attempts left and the guessed number is actually less than {guess}.')
        guesses_more_than_magic_number.append(guess)
        return True
    return False


def rotate_log_file():
    if os.path.exists(LOG_FILE) and os.path.getsize(LOG_FILE) > MAX_LOG_SIZE:
        with open(LOG_FILE, 'r') as f:
            lines = f.readlines()
        with open(LOG_FILE, 'w') as f:
            f.writelines(lines[-100:])  # Keep only the last 100 lines


def log_action(action_type, message, current_time=None):
    rotate_log_file()
    if current_time is None:
        current_time = datetime.now()
    time_now = current_time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]  # Include milliseconds and truncate to 3 decimal places
    log_line = f'[{time_now}][INFO][{action_type}]: {message}\n'
    with open(LOG_FILE, 'a') as file_log:
        file_log.write(log_line)


def save_magic_number(magic_number):
    log_action("System", f"Загадано число {magic_number}")


def save_guess(guess):
    log_action("User", f"Введено число {guess}")


def save_win():
    log_action("System", "Число угадано")


def save_count(count):
    log_action("System", f"Попыток: {count}")


def main():
    global count, magic_number
    print(f'A group of intellectuals guessed a number from 1 inclusive to 15 inclusive. You have 10 attempts to guess '
          'the number. And the game begins now...')
    save_magic_number(magic_number)
    while count < MAX_ATTEMPTS:
        try:
            guess = input("Guess the number if you can: ")
            save_guess(guess)
            guess = int(guess)
            print()
        except ValueError:
            print(f'You can only enter numbers.')
            continue
        if guess not in range(MIN_NUMBER, MAX_NUMBER + 1):
            print(f'The hidden number is from {MIN_NUMBER} inclusive to {MAX_NUMBER} inclusive.')
            continue
        count += 1
        if guess == magic_number:
            print(f'Congratulations! You guessed the number on the {count} try!')
            save_win()
            save_count(count)
            break
        confirm_magic_number_is_more_than_guess(guess, magic_number)
        confirm_magic_number_is_less_than_guess(guess, magic_number)
        print()
    else:
        print(f'Unfortunately, you have reached the maximum number of guessing attempts and lost.')
        save_count(count)

if __name__ == '__main__':
    main()
