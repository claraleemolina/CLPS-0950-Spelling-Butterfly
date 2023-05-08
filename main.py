dictionary_file = open("[path to words.txt file]", "r")

dictionary = []
for word in dictionary_file:
    dictionary.append(str(word.lower()[:-1]))

import string
alphabet = list(string.ascii_lowercase)

def spelling_butterfly(letters, center_letter):
    bad_letters = [n for n in alphabet if n not in letters]
    correct_words = []

    for word in dictionary:
        if center_letter in word:
            if word not in correct_words:
                if len(word) > 3:
                    if any(n in bad_letters for n in word) == False:
                        correct_words.append(word)

    return correct_words