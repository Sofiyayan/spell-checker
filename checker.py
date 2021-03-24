from functions import *
import linecache
import re


def creat_dict():
    soundex_dict = dict()
    leading_letter = "A"

    for alpha in range(0, 26):
        for i in range(0, 1000):
            soundex_dict["".join([leading_letter, str(i).zfill(3)])] = []
        leading_letter = chr(ord(leading_letter) + 1)
    return soundex_dict


def mapping(soundex_dict: dict):
    with open("../dictionary.txt", "r") as out_file:
        words = out_file.readlines()
    for word in words:
        soundex_code = soundex(word.strip())
        soundex_dict[soundex_code].append(word.strip())
    with open("../final.txt", "w") as new:
        for v in soundex_dict.items():
            new.write(str(v[1]) + "\n")


def soundex_matching(word: str) -> list:
    soundex_code = soundex(word)
    letter = soundex_code[:1]
    number = soundex_code[1:]
    with open("../final.txt", "r"):
        word_list = linecache.getline(
            "../final.txt", (ord(letter) - ord("A")) * 1000 + int(number) + 1
        )
    return re.sub("[^\w]", " ", word_list).split()


def levenshtein_minimizing(word: str, word_list) -> list:
    levenshtein_dict = {levenshtein(word, i): [] for i in word_list}
    for i in word_list:
        levenshtein_dict[levenshtein(word, i)].append(i)
    minimum = min(levenshtein_dict.keys())
    return levenshtein_dict.get(minimum)
