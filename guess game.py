import random

def print_message(message):
    print(message)

def get_difficulty():
    while True:
        try:
            difficulty = int(input("Pick a difficulty level (1, 2, or 3): "))
            if difficulty in [1, 2, 3]:
                return difficulty
            else:
                print_message("Please enter a valid difficulty level (1, 2, or 3).")
        except ValueError:
            print_message("Please enter a number.")

def start_game():
    difficulty = get_difficulty()
    number_of_guesses = 0
    max_number = 10 ** difficulty
    number = random.randint(1, max_number)
    
    print_message(f"Let's play Guess the Number! I'm thinking of a number between 1 and {max_number}.")
    
    while True:
        guess = input("Your Guess: ")
        try:
            guessed_number = int(guess)
            if 1 <= guessed_number <= max_number:
                number_of_guesses += 1
                if guessed_number == number:
                    print_message(f"You got it in {number_of_guesses} guesses!")
                    break
                elif guessed_number > number:
                    print_message("Too high. Guess again.")
                else:
                    print_message("Too low. Guess again.")
            else:
                print_message(f"Please enter a number between 1 and {max_number}.")
        except ValueError:
            print_message("Please enter a valid number.")
    
    play_again()

def play_again():
    answer = input("Play again? (y/n): ").lower()
    if answer == 'y':
        start_game()
    else:
        print_message("Goodbye!")

if __name__ == "__main__":
    start_game()
