print("""
Hello my darling,
I heard that taurus retrogate hits u harshly.
Nothing will be better than relaxing time with the perfect 
matching zodiac sign partner. No more surprises! Let's get start! \n""" )

import random
import string
zodiac = ["cancer", "taurus", "capricorn", "libra", "pisces", "leo", "escorpio", "capricornio", "geminis"]
ran_zodiac = random.choice(zodiac)
attempts = 2 * len(ran_zodiac)
print("Here u have some hints:\n")
final = " _ " * len(ran_zodiac)
print(f"The first letter of a zodiac is {ran_zodiac[0]}")
letters = []
words = []
guessed = False
print(final)
print("\n")

while attempts > 0 and not guessed:
    guess = input("Write a word or a letter: ").lower()
    print("")
    if len(guess) == 1 and guess.isalpha():
        if guess in letters:
            print(f"{guess} was already used.")
        elif guess not in ran_zodiac:
            print(f"Try again. No {guess} in the  sign.")
            attempts -= 1
            letters.append(guess)
        else:
            print(f"Muy bien! {guess} is in the sign" )
            letters.append(guess)
            separated = list(final)
            numer = [i for i, letter in enumerate(ran_zodiac) if letter == guess]
            for index in numer:
                separated[index] = guess
            final = "".join(separated)
            if "_" not in final:
                guessed = True

    elif len(guess) == len(ran_zodiac) and guess.isalpha():
        if guess in words:
            print("Tranquilo! You already know your match.")
        elif guess != ran_zodiac:
            print("Hold your horses! Guess is incorrect.")
            attempts -= 1
            words.append(guess)
        else:
            guessed = True
            final = ran_zodiac
    

    else:
        print("""Not this time. Go buy a cat""")

if guessed:
    print(f"""Wow u witch. Guessed with the first try. 
    Now you can look for {ran_zodiac} in tinder bios""")


else:
    print(f"Okay, maybe you should buy a cat? No more attempts.")