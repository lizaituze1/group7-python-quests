# Store the secret code that the user must guess
secret_code = 42

# Give the user three attempts
attempts = 3

# Continue the game while attempts remain
while attempts > 0:

    # Ask the user to guess the secret code
    guess = int(input("Guess the secret code: "))

    # Check if the guess is correct
    if guess == secret_code:
        print("Correct! You unlocked the code.")

        # End the game if the user guesses correctly
        break
    else:
        # Reduce the number of attempts after a wrong guess
        attempts -= 1

        print("Wrong guess!")

        # Show how many attempts remain
        if attempts > 0:
            print(f"You have {attempts} attempts left.")

# Display a message if the user uses all attempts
if attempts == 0:
    print("Game over! The secret code was 42.")