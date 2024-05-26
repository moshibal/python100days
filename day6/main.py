import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
# random number between 1 and 100 inclusive
random_number = random.randint(1, 100)


# constants
EASY = 10
HARD = 5
# attempts
number_of_attempts = 0
# difficulty
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
# condition to assign number_of_attempts
if difficulty.lower() == "easy":
    number_of_attempts = EASY
else:
    number_of_attempts = HARD

# loop to run until the number more than 0.
while number_of_attempts > 0:
    print(f"You have {number_of_attempts} attempts remaining to guess the number")
    guess_number = int(input("Make a guess: "))
    if guess_number == random_number:
        print("you have guessed right😘")
        number_of_attempts = 0
    else:

        if guess_number > random_number:
            print("you have guessed too high")
        else:
            print("you have guessed too low")
        number_of_attempts -= 1;
