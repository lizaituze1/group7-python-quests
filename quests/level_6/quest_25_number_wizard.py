# Import the random module to generate a random number
import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Keep asking the user until they guess correctly
while True:

    # Ask the user to guess the number
    guess = int(input("Guess the number (1-100): "))

    # Check if the guess is too high
    if guess > secret_number:
        print("Too high!")

    # Check if the guess is too low
    elif guess < secret_number:
        print("Too low!")

    # If the guess is correct, congratulate the user
    else:
        print("Congratulations! You guessed the number.")

        # Exit the loop since the game is over
        break