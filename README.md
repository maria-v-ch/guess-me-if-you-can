# Guess Me If You Can

"Guess Me If You Can" is an engaging text-based game that challenges players to guess a randomly generated number while providing thought-provoking quotes along the way. It's designed for those who enjoy a moment of interactive reflection or need a kind word during challenging times.

## Features

- Random number generation between 1 and 15
- User input validation
- Helpful hints (higher/lower) after each guess
- Maximum of 10 attempts per game
- Inspirational quotes displayed after each incorrect guess
- Logging of game actions and results with automatic log rotation
- Comprehensive test suite with 98% coverage

## Technologies and Creative Aspects

This project showcases the following creative elements and technologies:

- **Creative Game Design**: Combining number guessing with inspirational quotes for a unique user experience
- **Modular Code Structure**: Well-organized functions for easy maintenance and extensibility
- **Python 3.12**: Leveraging the latest Python features for efficient code
- **Random Module**: For generating unpredictable game numbers
- **JSON Handling**: Storing and retrieving quotes from a JSON file
- **File I/O**: Implementing a rotating log system to manage log file size
- **Datetime Module**: For precise timestamping in logs
- **Error Handling**: Graceful management of invalid user inputs
- **Unit Testing**: Comprehensive test suite using pytest and unittest.mock
- **Constants and Configuration**: Easy game customization through constants

## Installation

1. Ensure you have Python 3.12 installed on your system.
2. Clone this repository:
   ```
   git clone https://github.com/maria-v-ch/guess-me-if-you-can.git
   ```
3. Navigate to the project directory:
   ```
   cd guess-me-if-you-can
   ```
4. Create a virtual environment:
   ```
   python -m venv .venv
   ```
5. Activate the virtual environment:
   - On Windows: `.venv\Scripts\activate`
   - On macOS and Linux: `source .venv/bin/activate`
6. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

To start the game, run the following command in your terminal:

```
python main.py
```

Follow the on-screen instructions to play the game.

## Running Tests

To run the tests and check coverage:

1. Ensure you're in the project directory with the virtual environment activated.
2. Run the tests with coverage:
   ```
   coverage run -m pytest test_main.py
   ```
3. View the coverage report:
   ```
   coverage report -m
   ```

## Project Structure

- `main.py`: Contains the main game logic and helper functions
- `test_main.py`: Includes all unit tests for the game
- `sayings.json`: Stores the inspirational quotes
- `log.txt`: Log file for game actions (automatically rotated when size exceeds 1MB)
- `README.md`: Project documentation
- `.gitignore`: Specifies intentionally untracked files to ignore

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. An interesting branch to contribute to would be writing a bot that collects quotes by or from writers, philosophers, artists, technology leaders and innovators or in one word people who contribute to humanity with their life and work but also transmit their understanding of the world in short phrases with a lot of meaning.

Please make sure to update tests as appropriate and maintain or improve the current test coverage.

## License

[MIT](https://choosealicense.com/licenses/mit/)
