from main import confirm_magic_number_is_more_than_guess, confirm_magic_number_is_less_than_guess


def test_confirm_magic_number_is_more_than_guess():
    guess = 1
    magic_number = 2
    assert confirm_magic_number_is_more_than_guess(guess, magic_number) == True


def test_confirm_magic_number_is_more_than_guess():
    guess = 2
    magic_number = 1
    assert confirm_magic_number_is_more_than_guess(guess, magic_number) == False


def test_confirm_magic_number_is_less_that_guess():
    guess = 2
    magic_number = 1
    assert confirm_magic_number_is_less_than_guess(guess, magic_number) == True


def test_confirm_magic_number_is_less_that_guess():
    guess = 1
    magic_number = 2
    assert confirm_magic_number_is_less_than_guess(guess, magic_number) == False
