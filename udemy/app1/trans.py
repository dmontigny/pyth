#import os
import json
from difflib import SequenceMatcher, get_close_matches

#cwd = os.getcwd() + "git/pyth/udemy/app1/"

data = json.load(open("data.json", "r"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys(), cutoff = 0.8)) > 0:
        yn = input("Did you mean %s instead? (Y/n) " % get_close_matches(w, data.keys())[0])
        #yn = yn.upper()
        if yn.upper() == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn.upper() == "N":
            return "I do not recognize %s." % w
        else:
            return "Incorrect response. Exiting routine."
    else:
        return "I do not recognize %s." % w

word = input("Enter word :")

print(translate(word))

