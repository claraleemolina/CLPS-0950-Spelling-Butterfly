import english_words
import random
from math import floor
import cv2
import PIL
import tkinter as tk


web2lowerset = english_words.get_english_words_set(['web2'], lower=True)


def main():
    # sets up dictionary of all possible words
    # generate letters
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                  'z']
    seven_letters = random.sample(vowels, k=2) + random.sample(consonants, k=5)
    center_letter = random.choice(seven_letters)
    print(seven_letters, center_letter)

    # create answer function
    alphabet = vowels + consonants
    bad_letters = [n for n in alphabet if n not in seven_letters]

    def spelling_butterfly():
        correct_words = []

        for word in web2lowerset:
            if center_letter in word:
                if word not in correct_words:
                    if len(word) > 3:
                        if not any(n in bad_letters for n in word):
                            correct_words.append(word)

        return correct_words

    correct_words = spelling_butterfly()
    print(correct_words)

    def points_assign():
        # assigning points to all possible words
        points_correct_words = []
        for word in correct_words:
            points_correct_words.append(len(word))

        total_possible_points = sum(points_correct_words)

        print(points_correct_words)
        print(total_possible_points)

        points_per_rank = floor(total_possible_points / 9)
        remainder = total_possible_points % 9
        rank1 = points_per_rank * 1
        rank2 = points_per_rank * 2
        rank3 = points_per_rank * 3
        rank4 = points_per_rank * 4
        rank5 = points_per_rank * 5
        rank6 = points_per_rank * 6
        rank7 = points_per_rank * 7
        rank8 = points_per_rank * 8
        rank9= points_per_rank * 9 + remainder

        print(points_per_rank, remainder)
        print(rank1, rank2, rank3, rank4, rank5, rank6, rank7, rank8, rank9)

        if total_guessed_points == rank1 or (total_guessed_points < rank2 and total_guessed_points>rank1):
            print("i am rank 1!")
        elif total_guessed_points == rank2:
            print("i am rank 2!")
        else:
            print(" i am rankless")


    # rank assignments
    # if no possible points, no ranks
    # if possible points are less than 9, then reach rank of butterfly after all points acquired
    # if possible points are greater than 9,
    #   divide total possible points by 9
    #   divvy up ranks by rounding to nearest point value of division
    #   if word causes a move-up in more than one rank, only display the highest rank


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




        # assigning points to all guessed words; must figure out how to embed this within gameplay
        points_correct_guesses = []
        for guess in correct_guesses:
            points_correct_guesses.append(len(guess))

        total_guessed_points = sum(points_correct_guesses)

        print(points_correct_guesses)
        print(total_guessed_points)

        points_assign()

# affirmation based on word length
#   words of length 4 result in 'Good!'
#   words of length 5 result in 'Nice!'
#   words of length 6 and above result in 'Amazing!'

if __name__ == "__main__":
    main()

