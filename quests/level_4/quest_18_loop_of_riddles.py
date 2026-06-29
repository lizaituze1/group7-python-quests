# Quest 18: The Loop of Riddles
# Guessing game: keep asking until the user guesses the secret number.
secret_number = 7

guess = int(input("Guess my number (1-10): "))
while guess != secret_number:
    print("Nope, try again!")
    guess = int(input("Guess my number (1-10): "))

print("You got it! The number was", secret_number)
