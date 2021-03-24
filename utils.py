import sys


def levenshtein(str_1, str_2):
    levenshtein_array = [i for i in range(len(str_1) + 1)]
    for i in range(1, len(str_2) + 1):
        levenshtein_array_new = [i]
        for j in range(1, len(str_1) + 1):
            if str_1[j - 1] == str_2[i - 1]:
                levenshtein_array_new += [
                    min(
                        levenshtein_array[j - 1],
                        levenshtein_array[j] + 1,
                        levenshtein_array_new[j - 1] + 1,
                    )
                ]
            else:
                levenshtein_array_new += [
                    min(
                        levenshtein_array[j - 1],
                        levenshtein_array[j],
                        levenshtein_array_new[j - 1],
                    )
                    + 1
                ]

        levenshtein_array = levenshtein_array_new
    return levenshtein_array[-1]


def soundex(input_str):
    code = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 0,
        "F": 1,
        "G": 2,
        "H": 0,
        "I": 0,
        "J": 2,
        "K": 2,
        "L": 4,
        "M": 5,
        "N": 5,
        "O": 0,
        "P": 1,
        "Q": 2,
        "R": 6,
        "S": 2,
        "T": 3,
        "U": 0,
        "V": 1,
        "W": 0,
        "X": 2,
        "Y": 0,
        "Z": 2,
    }

    upper = input_str.upper()
    soundex_code = [upper[0]]
    for i in range(1, len(upper)):
        if len(soundex_code) < 4:
            if not upper[i].isalpha():
                print("Input for soundex function should only contain letters with no space")
                sys.exit()
            elif code.get(upper[i]) != 0 and code.get(upper[i - 1]) != code.get(
                upper[i]
            ):
                soundex_code.append(str(code.get(upper[i])))
            else:
                continue
        else:
            break
    if len(soundex_code) < 4:
        soundex_code.append("0" * (4 - len(soundex_code)))
    return "".join(soundex_code)
