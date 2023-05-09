import string
import random

# sets up dictionary of all possible words
dictionary_file = open("words.txt", "r")

# generate letters
letter_generator = string.ascii_lowercase
seven_letters = random.sample(letter_generator, k=7)
center_letter = random.choice(seven_letters)

# create answer function


def spelling_butterfly(seven_letters, center_letter):

    dictionary = []
    for word in dictionary_file:
        dictionary.append(str(word.lower()[:-1]))

    alphabet = list(string.ascii_lowercase)

    bad_letters = [n for n in alphabet if n not in seven_letters]
    correct_words = []

    for word in dictionary:
        if center_letter in word:
            if word not in correct_words:
                if len(word) > 3:
                    if not any(n in bad_letters for n in word):
                        if '.' not in word and '-' not in word:
                            correct_words.append(word)

    return correct_words


print(spelling_butterfly(seven_letters, center_letter))

# New window code
# Window of Rules #


from tkinter import *


#Create an instance of tkinter frame
win= Tk()


#Set the geometry
win.geometry("750x280")


#Create a canvas object
canvas= Canvas(win, width= 1000, height= 750, bg="white")


#Add a text in Canvas
canvas.create_text(300, 50, text="GAME RULES", fill="black", font=('Helvetica 15 bold'))
canvas.pack()


win.mainloop()


# gameplay


correct_guesses = []
if guess in correct_words:
    if center_letter not in guess:
        print("Missing center letter")
    elif len(guess) > 3:
        print("Too short")
    elif not any(n in bad_letters for n in guess) and 'n' not in guess and '-' not in guess:
        print("Bad letters")
    else:
        print("Good!")
        correct_guesses.append(guess)
else:
    print("Not in word list")