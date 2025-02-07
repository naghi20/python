import random as diceroll # Import the Random module 
import time  # Import the time module for the timer

# Function to prompt and return user's guess
def getUserGuess(min_val, max_val):
    while True:
        try:
            user_input = input(f"What do you think the dice rolled value is from ({min_val} to {max_val})? (Type 'quit' to give up): ")
            if user_input.lower() == 'quit':
                return None  # User wants to quit
            user_guess = int(user_input)
            if min_val <= user_guess <= max_val:
                return user_guess
            else:
                print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a valid number or 'quit' to give up.")

# Function to validate yes/no inputs
def getYesNoInput(prompt):
    while True:
        user_input = input(prompt).lower()
        if user_input in ['yes', 'no']:
            return user_input == 'yes'
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# Function to play a single round of the game
def playRound(difficulty_levels, difficulty, hints_enabled):
    # Set the game parameters based on the chosen difficulty
    min_val = difficulty_levels[difficulty]["min_val"]
    max_val = difficulty_levels[difficulty]["max_val"]
    max_attempts = difficulty_levels[difficulty]["max_attempts"]

    # Simulate a dice being rolled, random result between min_val and max_val (inclusive)
    randomDiceRollResult = diceroll.randint(min_val, max_val)

    print(f"Let's begin! You have {max_attempts} attempts to guess the number between {min_val} and {max_val}.")

    attempts = 0

    # Start the timer (10 seconds per attempt)
    start_time = time.time()
    time_limit = 10 * max_attempts  # Total time limit for all attempts

    while attempts < max_attempts:
        elapsed_time = time.time() - start_time
        if elapsed_time >= time_limit:
            print("Time's up! You ran out of time.")
            break

        your_guess = getUserGuess(min_val, max_val)
        
        if your_guess is None:  # User chose to quit
            print(f"You gave up! The correct number was {randomDiceRollResult}.")
            return False  # User lost this round
        
        attempts += 1
        
        if your_guess == randomDiceRollResult:
            print("Correct! You win!")
            return True  # User won this round
        elif hints_enabled:
            if your_guess < randomDiceRollResult:
                print("Nope! Your guess is too low.")
            else:
                print("Nope! Your guess is too high.")
        else:
            print("Nope! Try again.")
    
    if attempts == max_attempts:
        print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {randomDiceRollResult}.")
    
    return False  # User lost this round

############################## MAIN application code ######################
print("Welcome to the Dice Guessing Game!")

# Define difficulty levels
difficulty_levels = {
    "easy": {"min_val": 1, "max_val": 10, "max_attempts": 7},
    "medium": {"min_val": 1, "max_val": 50, "max_attempts": 5},
    "hard": {"min_val": 1, "max_val": 100, "max_attempts": 3}
}

# Let the user choose a difficulty level with validation
while True:
    difficulty = input("Choose a difficulty level (easy, medium, hard): ").lower()
    if difficulty in difficulty_levels:
        break
    else:
        print("Invalid difficulty level. Please choose 'easy', 'medium', or 'hard'.")

# Ask if the user wants hints with validation
hints_enabled = getYesNoInput("Would you like hints (too high/too low)? (yes/no): ")

# Initialize variables for multiple rounds
round_number = 1
total_wins = 0

while True:
    print(f"\n--- Round {round_number} ---")
    
    # Play a round and check if the user won or lost
    if playRound(difficulty_levels, difficulty, hints_enabled):
        total_wins += 1
    
    # Ask if the user wants to play another round with validation
    play_again = getYesNoInput("\nDo you want to play another round? (yes/no): ")
    
    if not play_again:
        break
    
    round_number += 1

# Display final results after all rounds are played
print("\nGame over!")
print(f"You played {round_number} rounds and won {total_wins} of them!")
