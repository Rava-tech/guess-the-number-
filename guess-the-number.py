import random

number = random.randint(1, 100)

while True:
    guess = input("Guess the number: ")

    if not guess.isdigit():
        print("It's not a number!")
        continue

    guess = int(guess)

    if guess < number:
        print("To small!")
    elif guess > number:
        print("To big!")
    else:
        print("You win!")
        break
