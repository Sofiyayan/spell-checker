from functions import *


def menu():
    user_choice = input(
        "Choose from options:\n 1. Levenshtein \n 2. Soundex \n 3. Spell correction \n Type 1, 2 or 3: \n"
    )
    return user_choice


def call_levenshtein():
    first_string = input("First string: ")
    second_string = input("Second string: ")
    print(
        'Levenshtein distance for "{}" and "{}" is {}'.format(
            first_string,
            second_string,
            levenshtein(first_string, second_string),
        )
    )


def call_soundex():
    string_1 = input("Input string: ")
    print('Soundex code for "{}" is {}'.format(string_1, soundex(string_1)))


def call_spell_correction():
    misspelled = input("Write misspelled word: ")
    print(
        "Possible options: {}".format(
            (levenshtein_minimizing(misspelled, soundex_matching(misspelled)))
        )
    )


if __name__ == "__main__":
    number = menu()
    if number.strip() == "1":
        call_levenshtein()
    elif number.strip() == "2":
        call_soundex()
    elif number.strip() == "3":
        call_spell_correction()
    else:
        print("Input number is not in the menu")
