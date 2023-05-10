import english_words
import random

# sets up dictionary of all possible words
web2lowerset = english_words.get_english_words_set(['web2'], lower=True)

# generate letters
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'z']
seven_letters = random.sample(vowels, k=2) + random.sample(consonants, k=5)
center_letter = random.choice(seven_letters)
print(seven_letters, center_letter)

# create answer function
alphabet = vowels + consonants
bad_letters = [n for n in alphabet if n not in seven_letters]


def spelling_butterfly(seven_letters, center_letter):
    correct_words = []

    for word in web2lowerset:
        if center_letter in word:
            if word not in correct_words:
                if len(word) > 3:
                    if not any(n in bad_letters for n in word):
                        correct_words.append(word)

    return correct_words


correct_words = spelling_butterfly(seven_letters, center_letter)
print(correct_words)


# gameplay rough draft
correct_guesses = []
while len(correct_guesses) < len(correct_words):
    guess = input("Write guess ")

    if str(guess) in web2lowerset:
        if str(center_letter) not in str(guess):
            print("Missing center letter")
        elif len(guess) < 3:
            print("Too short")
        elif any(n in bad_letters for n in str(guess)):
            print("Bad letters")
        elif str(guess) in correct_guesses:
            print("Already found")
        elif str(guess) in correct_words:
            print("Good!")
            correct_guesses.append(str(guess))
            print(correct_guesses)
    else:
        print("Not in word list")

# Window of Rules #
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
root = tk.Tk()
root.title("Game Rules")
st = ScrolledText(root, width=50,  height=10)
st.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

root.mainloop()
