import pytest
from unittest.mock import patch, mock_open, call
from datetime import datetime
from main import (
    confirm_magic_number_is_more_than_guess,
    confirm_magic_number_is_less_than_guess,
    print_random_saying,
    rotate_log_file,
    log_action,
    save_magic_number,
    save_guess,
    save_win,
    save_count,
    LOG_FILE
)


def test_confirm_magic_number_is_more_than_guess():
    assert confirm_magic_number_is_more_than_guess(1, 2) == True
    assert confirm_magic_number_is_more_than_guess(2, 1) == False
    assert confirm_magic_number_is_more_than_guess(2, 2) == False


def test_confirm_magic_number_is_less_than_guess():
    assert confirm_magic_number_is_less_than_guess(2, 1) == True
    assert confirm_magic_number_is_less_than_guess(1, 2) == False
    assert confirm_magic_number_is_less_than_guess(2, 2) == False


@patch('main.random.choice')
def test_print_random_saying(mock_choice):
    mock_choice.return_value = "Test saying"
    with patch('builtins.print') as mock_print:
        print_random_saying()
        mock_print.assert_called_once_with("Test saying")


@patch('os.path.exists')
@patch('os.path.getsize')
@patch('builtins.open', new_callable=mock_open)
def test_rotate_log_file(mock_file, mock_getsize, mock_exists):
    mock_exists.return_value = True
    mock_getsize.return_value = 2 * 1024 * 1024  # 2 MB
    mock_file().readlines.return_value = ['line1\n', 'line2\n', 'line3\n']
    
    rotate_log_file()
    
    mock_file().writelines.assert_called_once_with(['line1\n', 'line2\n', 'line3\n'])


@patch('os.path.exists')
@patch('os.path.getsize')
@patch('builtins.open', new_callable=mock_open)
def test_rotate_log_file_small_file(mock_file, mock_getsize, mock_exists):
    mock_exists.return_value = True
    mock_getsize.return_value = 100  # Smaller than MAX_LOG_SIZE
    rotate_log_file()
    mock_file.assert_not_called()


@patch('main.datetime')
@patch('builtins.open', new_callable=mock_open)
def test_log_action(mock_file, mock_datetime):
    mock_now = datetime(2023, 1, 1, 12, 0, 0, 123000)
    
    log_action("Test", "Test message", current_time=mock_now)
    
    expected_log_line = '[2023-01-01 12:00:00.123][INFO][Test]: Test message\n'
    mock_file.assert_called_once_with(LOG_FILE, 'a')
    mock_file().write.assert_called_once_with(expected_log_line)
    
    actual_call = mock_file().write.call_args[0][0]
    print(f"Expected: {expected_log_line}")
    print(f"Actual: {actual_call}")
    assert actual_call == expected_log_line


@patch('main.log_action')
def test_save_functions(mock_log_action):
    save_magic_number(42)
    mock_log_action.assert_called_with("System", "Загадано число 42")
    
    save_guess(7)
    mock_log_action.assert_called_with("User", "Введено число 7")
    
    save_win()
    mock_log_action.assert_called_with("System", "Число угадано")
    
    save_count(5)
    mock_log_action.assert_called_with("System", "Попыток: 5")


@patch('builtins.input', side_effect=['8', '12', '10'])
@patch('main.random.randint', return_value=10)
@patch('main.print')
@patch('main.save_magic_number')
@patch('main.save_guess')
@patch('main.save_win')
@patch('main.save_count')
def test_main_game_loop(mock_save_count, mock_save_win, mock_save_guess, mock_save_magic_number, mock_print, mock_randint, mock_input):
    import main
    main.magic_number = 10  # Set the magic number explicitly
    main.count = 0  # Reset the count
    main.main()
    mock_save_magic_number.assert_called_once_with(10)
    assert mock_save_guess.call_count == 3
    mock_save_win.assert_called_once()
    mock_save_count.assert_called_once_with(3)

@patch('builtins.input', side_effect=['1', '2', '3', '4', '5', '6', '7', '8', '9', '15'])
@patch('main.random.randint', return_value=10)
@patch('main.print')
@patch('main.save_magic_number')
@patch('main.save_guess')
@patch('main.save_count')
def test_main_game_loop_lose(mock_save_count, mock_save_guess, mock_save_magic_number, mock_print, mock_randint, mock_input):
    import main
    main.magic_number = 10  # Set the magic number explicitly
    main.count = 0  # Reset the count
    main.main()
    mock_save_magic_number.assert_called_once_with(10)
    assert mock_save_guess.call_count == 10
    mock_save_count.assert_called_once_with(10)

@patch('main.print')
@patch('main.print_random_saying')
def test_confirm_magic_number_is_more_than_guess_equal(mock_print_saying, mock_print):
    result = confirm_magic_number_is_more_than_guess(5, 5)
    assert result == False
    mock_print.assert_not_called()
    mock_print_saying.assert_not_called()

@patch('main.print')
@patch('main.print_random_saying')
def test_confirm_magic_number_is_less_than_guess_equal(mock_print_saying, mock_print):
    result = confirm_magic_number_is_less_than_guess(5, 5)
    assert result == False
    mock_print.assert_not_called()
    mock_print_saying.assert_not_called()

@patch('json.load')
@patch('builtins.open', new_callable=mock_open)
def test_print_random_saying_load_json(mock_file, mock_json_load):
    mock_json_load.return_value = ["Test saying 1", "Test saying 2"]
    with patch('random.choice', return_value="Test saying 1"):
        print_random_saying()
    mock_file.assert_called_once_with('sayings.json', 'r')
    mock_json_load.assert_called_once()

@patch('builtins.input', side_effect=['not a number', '10'])
@patch('main.random.randint', return_value=10)
@patch('main.print')
@patch('main.save_magic_number')
@patch('main.save_guess')
@patch('main.save_win')
@patch('main.save_count')
def test_main_game_loop_value_error(mock_save_count, mock_save_win, mock_save_guess, mock_save_magic_number, mock_print, mock_randint, mock_input):
    import main
    main.magic_number = 10  # Set the magic number explicitly
    main.count = 0  # Reset the count
    main.main()
    mock_save_magic_number.assert_called_once_with(10)
    assert mock_save_guess.call_count == 2
    mock_save_win.assert_called_once()
    mock_save_count.assert_called_once_with(1)
