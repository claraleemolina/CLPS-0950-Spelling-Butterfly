dictionary_file = open("words.txt", "r")

# print("Data type before reconstruction : ", type(data))
	
# js = json.loads(data)

# print("Data type after reconstruction : ", type(js))
# print(js)


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

#To git commmit and push, type the following lines into your terminal
# git add -A
# git commit -m "any messsage you want"
# git push

#If your partner pushes code
# git pull

#If you have made any changes but you do not want to push them
# git stash #

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
winwHeight = window.winfo_reqheight()
posRight = int(window.winfo_screenwidth() / 2 - winWidth / 2)
posDown = int(window.winfo_screenheight() / 2 - winwHeight / 2)
window.geometry("+{}+{}".format(posRight, posDown))
window.mainloop()