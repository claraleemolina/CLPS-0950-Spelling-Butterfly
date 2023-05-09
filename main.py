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

# Window of Rules #
from tkinter import *
window = Tk()
window.title("Game Rules")
window.configure(bg='white')
window.mainloop()
import Tkinter as Tk
label = Tk.Label(None, text='Blah blah blah', font=('Times', '18'),fg='blue')
label.pack()
label.mainloop()
# move window center
winWidth = window.winfo_reqwidth()
winHeight = window.winfo_reqheight()
posRight = int(window.winfo_screenwidth() / 2 - winWidth / 2)
posDown = int(window.winfo_screenheight() / 2 - winHeight / 2)
window.geometry("+{}+{}".format(posRight, posDown))
window.mainloop()

# gameplay
