import json
import random
from datetime import datetime

count = 0
threshold = 10
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


def save_magic_number():
    with open('log.txt', 'a') as file_log:
        log_line = [f'[{time_now}][INFO][System]: Загадано число {magic_number} \n']
        file_log.writelines(log_line)


def save_guess():
    with open('log.txt', 'a') as file_log:
        log_line = [f'[{time_now}][INFO][User]: Введено число {guess} \n']
        file_log.writelines(log_line)


def save_win():
    with open('log.txt', 'a') as file_log:
        log_line = [f'[{time_now}][INFO][System]: Число угадано \n']
        file_log.writelines(log_line)


def save_count():
    with open('log.txt', 'a') as file_log:
        log_line = [f'Попыток: {count}\n']
        file_log.writelines(log_line)


if __name__ == '__main__':

    sayings_list = ["Rather than love, than money, than fame, give me truth. (с) Henry David Thoreau", "In any case you"
                    " must not confuse a single failure with a final defeat. (c) F. Scott Fitzgerald", "Talent hits a "
                    "target no one else can hit; Genius hits a target no one else can see. (c) Arthur Schopenhauer",
                    "All that happens means something; nothing you do is ever insignificant. (c) Aldous Huxley",
                    "Whoever wishes to go down a long path, must learn that the first lesson is to overcome early "
                    "disappointments. (c) Paulo Coelho", "Not everything that is faced can be changed, but nothing can "
                    "be changed until it is faced. (c) James Baldwin", "A wise man will make more opportunities, than "
                    "he finds. (c) Francis Bacon", "You will do foolish things, but do them with enthusiasm. (c) "
                    "Colette", "Instead of chopping yourself down to fit the world, chop the world down to fit "
                    "yourself. (c) D.H. Lawrence", "Mostly it is loss which teaches us about the worth of things. "
                    "(c) Arthur Schopenhauer", "Keep your face always toward the sunshine, and shadows will fall "
                    "behind you. (c) Walt Whitman", "The first principle is that you must not fool yourself, and you "
                    "are the easiest person to fool. (c) Richard Feynman", "Life is like playing a violin solo in "
                    "public and learning the instrument as one goes on. (c) Samuel Butler", "Forces beyond your "
                    "control can take away everything you possess except one thing, your freedom to choose how you "
                    "will respond to the situation. (c) Viktor Frankl", "The worst enemy to creativity is self-doubt."
                    " (c) Sylvia Plath", "You are what you do, not what you say you will do. (c) Carl Jung",
                    "You cannot swim for new horizons until you have courage to lose sight of the shore. (c) "
                    "William Faulkner", "Every generation imagines itself to be more intelligent than the one that "
                    "went before it, and wiser than the one that comes after it. (c) George Orwell", "Do not ever"
                    " tell anybody anything. If you do, you start missing everybody. (c) J. D. Salinger",
                    "There are two ways of spreading light: to be the candle or the mirror that reflects it. "
                    "(c) Edith Wharton", "Some of us think holding on makes us strong; but sometimes it is letting "
                    "go. (c) Hermann Hesse", "You cannot measure the mutual affection of two human beings by the "
                    "number of words they exchange. (c) Milan Kundera", "If we wait for the moment when everything, "
                    "absolutely everything is ready, we shall never begin. (c) Ivan Turgenev", "Life shrinks or "
                    "expands in proportion to one's courage. (c) Anaïs Nin", "Genius is nothing more nor less than "
                    "childhood recaptured at will. (c) Charles Baudelaire", "The world breaks everyone, and afterward,"
                    " many are strong at the broken places. (c) Ernest Hemingway", "Beware of those who seek constant"
                    " crowds; they are nothing alone. (c) Charles Bukowski", "My imagination functions much "
                    "better when I don't have to speak to people. (c) Patricia Highsmith", "I don't know why we are"
                    " here, but I'm pretty sure that it is not in order to enjoy ourselves. (c) Ludwig "
                    "Wittgenstein", "Love all, trust a few, do wrong to none. (c) William Shakespeare", "If it is not "
                    "right, do not do it; if it is not true, do not say it. (c) Marcus Aurelius", "I have a deeply"
                    " hidden and inarticulate desire for something beyond the daily life. (c) Virginia Woolf",
                    "All of humanity's problems stem from man's inability to sit quietly in a room alone. "
                    "(c) Blaise Pascal", "To be alive at all is to have scars. (c) John Steinbeck", "Ever tried. "
                    "Ever failed. No matter. Try again. Fail again. Fail better. (c) Samuel Beckett",
                    "Loneliness does not come from having no people about one, but from being unable to communicate"
                    " the things that seem important to oneself. (c) Carl Jung", "Nobody realizes that some people"
                    " expend tremendous energy merely to be normal. (c) Albert Camus", "Learn what is to be taken"
                    " seriously and laugh at the rest. (c) Hermann Hesse", "Whatever you're meant to do, do it now."
                    " The conditions are always impossible. (c) Doris Lessing", "Man is least himself when he talks "
                    "in his own person. Give him a mask, and he will tell the truth. (c) Oscar Wilde", "It may be "
                    "unfair, but what happens in a few days, sometimes even a single day, can change the course"
                    " of a whole lifetime. (c) Khaled Hosseini", "Let everything happen to you: beauty and terror. "
                    "Just keep going. No feeling is final. (c) Rainer Maria Rilke", "At the bottom of every frozen "
                    "heart there is a drop or two of love - just enough to feed the birds. (c) Henry Miller",
                    "One day I will find the right words, and they will be simple. (c) Jack Kerouac"]

    with open('sayings.json', 'w') as file:
        json.dump(sayings_list, file)

    print(f'A group of intellectuals guessed a number from 1 inclusive to 15 inclusive. You have 10 attempts to guess '
          'the number. And the game begins now...')
    save_magic_number()
    while count <= threshold:
        try:
            guess = input("Guess the number if you can: ")
            save_guess()
            guess = int(guess)
            print()
        except ValueError:
            print(f'You can only enter numbers.')
        if guess not in range(1, 16):
            print(f'The hidden number is from 1 inclusive to 15 inclusive.')
            continue
        count += 1
        if guess == magic_number:
            print(f'Congratulations! You guessed the number on the {count} try!')
            save_win()
            save_count()
            break
        confirm_magic_number_is_more_than_guess(guess, magic_number)
        confirm_magic_number_is_less_than_guess(guess, magic_number)
        print()
    else:
        print(f'Unfortunately, you have reached the maximum number of guessing attempts and lost.')
