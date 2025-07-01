import random

def guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100... can you guess it?")

    secret = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Enter your guess: ")

        try:
            guess = int(guess)
        except:
            print("Please enter a valid number!")
            continue

        attempts += 1

        if guess < secret:
            print("Too low! Try again.")
        elif guess > secret:
            print("Too high! Try again.")
        else:
            print(f"🎉 You got it in {attempts} tries! The number was {secret}.")
            break

guessing_game()