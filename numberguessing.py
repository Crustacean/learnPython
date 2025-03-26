
import random

start = 1
end = 100

print("Welcome to the Number Guessing game.")
print(f"I'm thinking of a number between {start} and {end}.")

number_to_guess = random.randint(start, end)

guess = None

number_of_retries = -1

play = input("Choose a difficulty. Type 'easy' or 'hard': ")

if play == "easy":
    number_of_retries = 10
elif play == "hard":
    number_of_retries = 5

while number_of_retries > 0 or guess != number_to_guess:
    print(f"You have {number_of_retries} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess == number_to_guess:
        print(f"You got it! The answer was {number_to_guess}.")        
    elif guess != number_to_guess:
        if guess < number_to_guess:
            print("Too low.")
            print("Guess again.")
        elif guess < number_to_guess:
            print("Too high.")
            print("Guess again.")
        
        number_of_retries -= 1

if number_of_retries == 0 and guess != number_to_guess:
    print("You've run out of guesses.")
