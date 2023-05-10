import english_words
import random

# Window of Rules #
from tkinter import *

root = Tk()
root.geometry("300x200")

w = Label(root, text ='GeeksForGeeks', font = "50")
w.pack()
	
msg = Message( root, text = "A computer science portal for geeks")
	
msg.pack()

root.mainloop()


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

# within spelling_butterfly function?
# length of each item in correct_words is equal to its point value
#   points_correct_words = []
#   map len(word) in correct_words onto points_correct_words
# where does points_correct_words fit into everything?
# sum of total points divided by number of items in correct_words determines ranks
# must have a way to pool ranks together if total number of words is very small
#   possibly a loop - if number of items in correct_words is _, then fewer ranks?
# length of each guess in correct_guesses is equal to its point value
# affirmation based on word length
#   words of length 4 result in 'Good!'
#   words of length 5 result in 'Nice!'
#   words of length 6 and above result in 'Amazing!'

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

