#Select a random between 10 and 20 number, user should input until the number is hit.
#Auther: Yang Yue

# This program generates a random number between 10 and 20 and prompts the user to guess it
import random

# Generate a random number between 10 and 20
secret_number = random.randint(10, 20)

print("I'm thinking of a number between 10 and 20. Can you guess it?")

# Loop until the user guesses the correct number
while True:
    try:
        guess = int(input("Enter your guess: "))
        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number}!")
            break
        elif guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")
    except ValueError:
        print("Please enter a valid number.")
