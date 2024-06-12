import random

def guess_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guessing Game!")
    print("I have chosen a number between 1 and 100.")

    while True:
        guess = int(input("Enter your guess: "))

        # Increment the number of attempts
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        guess_number()
    else:
        print("Thanks for playing!")

guess_number()