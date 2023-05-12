import english_words
import random
from math import floor
from PIL import Image

# sets up dictionary of all possible words
web2lowerset = english_words.get_english_words_set(['web2'], lower=True)


def main():
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

        # ranking system
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
        rank9 = points_per_rank * 9 + remainder

        print(points_per_rank, remainder)
        print(rank1, rank2, rank3, rank4, rank5, rank6, rank7, rank8, rank9)

        # assigning ranks based on points
        if total_guessed_points == rank1 or (total_guessed_points < rank2 and total_guessed_points > rank1):
            im = Image.open("/Users/claraleemolina/PycharmProject/CLPS-0950-Spelling-Butterfly/rank1.png")
            im.show()
        elif total_guessed_points == rank2 or (total_guessed_points < rank3 and total_guessed_points > rank2):
            im = Image.open("/Users/claraleemolina/PycharmProject/CLPS-0950-Spelling-Butterfly/rank2.png")
            im.show()
        elif total_guessed_points == rank3 or (total_guessed_points < rank4 and total_guessed_points > rank3):
            im = Image.open("/Users/claraleemolina/PycharmProject/CLPS-0950-Spelling-Butterfly/rank3.png")
            im.show()
        elif total_guessed_points == rank4 or (total_guessed_points < rank5 and total_guessed_points > rank4):
            im = Image.open("/Users/claraleemolina/PycharmProject/CLPS-0950-Spelling-Butterfly/rank4.png")
            im.show()
        elif total_guessed_points == rank5 or (total_guessed_points < rank6 and total_guessed_points > rank5):
            im = Image.open("/Users/claraleemolina/PycharmProject/CLPS-0950-Spelling-Butterfly/rank5.png")
            im.show()
        elif total_guessed_points == rank6 or (total_guessed_points < rank7 and total_guessed_points > rank6):
            im = Image.open("/Users/claraleemolina/PycharmProject/CLPS-0950-Spelling-Butterfly/rank6.png")
            im.show()
        elif total_guessed_points == rank7 or (total_guessed_points < rank8 and total_guessed_points > rank7):
            im = Image.open("/Users/claraleemolina/PycharmProject/CLPS-0950-Spelling-Butterfly/rank7.png")
            im.show()
        elif total_guessed_points == rank8 or (total_guessed_points < rank9 and total_guessed_points > rank8):
            im = Image.open("/Users/claraleemolina/PycharmProject/CLPS-0950-Spelling-Butterfly/rank8.png")
            im.show()
        elif total_guessed_points == rank9:
            im = Image.open("/Users/claraleemolina/PycharmProject/CLPS-0950-Spelling-Butterfly/rank9.png")
            im.show()
        else:
            print("Keep playing to level up!")

    # game loop
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

        # assigning points to all guessed words
        points_correct_guesses = []
        for guess in correct_guesses:
            points_correct_guesses.append(len(guess))

        total_guessed_points = sum(points_correct_guesses)

        print(points_correct_guesses)
        print(total_guessed_points)

        points_assign()

if __name__ == "__main__":
    main()

