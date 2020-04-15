# Programmed by Bilal Mahmood (github ghostinthetoast)

import json
import difflib
from difflib import get_close_matches

dictionary_data = json.load(open("data.json"))
word = ''

def translate(word):
    return(dictionary_data[word])

while word != 'q':
    word = input("\nPlease enter the word you would like to lookup, or type 'q' to quit. : ")
    word = word.lower()

    if word == 'q':
        exit(0)

    if word in dictionary_data:
        print(translate(word))
    else:
        closest_word = get_close_matches(word, dictionary_data.keys())[0]
        response = input("'" + word + "' is not in the dictionary. Did you mean '" + closest_word + "'? [y or n]: ")
        if response == "y":
            print(translate(closest_word))
        else:
            print("Sorry, your word is either not spelled correctly or not in the dictionary.")