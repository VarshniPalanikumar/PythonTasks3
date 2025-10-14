import random

word = ['python','javascript','java','automation','pytest', 'guvi', 'selenium']
random.shuffle(word)

for i in word:
    letters=list(i)
    random.shuffle(letters)
    scrambled="".join(letters)
    print(f"scrambled word: {scrambled}")
    guess=input("Guess the scrambled word: ")
    if guess.lower()== i:
        print("Hurray!!! you guessed it correctly!!")
    else:
        print(f"Oops its Wrong!!!. The correct word is: {i}")


