import random
'''Number Guessing Game'''
num= random.randrange(0,100)

for i in range(10):
    guess = int(input("Guess a number between 0 and 100: "))
    if guess < num:
        print(f"{guess} is too low")
    elif guess > num:
        print(f"{guess} is too high")
    else:
        print(f"Hurray!!!Guessed number {num} is correct")
        break





