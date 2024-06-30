import random


def guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    score = 100
    max_attempts = 10

    print("Guess the number between 1 and 100!")
    print(f"You have {max_attempts} attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Out of bounds! Please guess a number between 1 and 100.")
                continue

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                print(f"Your score is: {score}")
                break

            score -= 10

        except ValueError:
            print("Invalid input. Please enter a number.")

    if attempts == max_attempts:
        print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")


guessing_game()
