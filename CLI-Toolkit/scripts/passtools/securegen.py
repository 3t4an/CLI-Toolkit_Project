import random
import os

def securegen(args):

    if "-remove" in args:
        REMOVE = args.pop("-remove")
        REMOVE = [(type.upper() if len(type) > 1 else type) for type in REMOVE]
    else:
        REMOVE = []

    LENGTH = int(args["-length"][0])

    # 3 Characteristics of a Strong Password:
    # 1. Cannot be guessed
    # 2. Difficult to brute force
    # 3. Must be complicated

    # GOALS
    # 1. ["a", "b", "c", "d", "e" .. ] apply rules
    # 2. 0293if9023fi gneerate

    chars = {
        "UPPER":"ABCDEFGHIJKLMNOPQRSTUVWYXZ",
        "LOWER":"abcdefghijklmnopqrstuvwyxz",
        "NUMBERS":"1234567890",
        "SYMBOLS":"!@#$%^&*()"
    }

    # STEP 1
    chars = [char for type, characters in chars.items() for char in characters if type not in REMOVE]
    chars = [char for char in chars if char not in REMOVE]

    # STEP 2
    result = ""
    for _ in range(LENGTH):
        char = random.choice(chars)
        result = result+char
        chars.remove(char)

    
    if "-file" in args:
        FILE = args["-file"][0]
        DIR = os.path.dirname(os.path.abspath(__file__))
        DIR = os.path.dirname(DIR)
        DIR = os.path.join(DIR, "data")
        with open(f"{DIR}\{FILE}.txt", "w") as file:
            file.write(result)

    return result