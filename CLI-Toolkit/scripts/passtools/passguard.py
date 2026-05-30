def passguard(args):

    # GOALS:
    # 1. scan presented password for undeisrables
    # 2. return results

    # HOW TO CHECK A PASSWORD:
    # Length - makes difficult to reproduce or brute force - min 10
    # UNPREDICTIBILITY - makes difficult to reproduce or brute force
    # COMPLEXITY - diversity in characters

    passwords = args["-pass"]
    chars = {
        "UPPER":"ABCDEFGHIJKLMNOPQRSTUVWYXZ",
        "LOWER":"abcdefghijklmnopqrstuvwyxz",
        "NUMBERS":"1234567890",
        "SYMBOLS":"!@#$%^&*()"
    }
    results = {}

    # GOAL 1

    for password in passwords:
        # CHECK 1
        result = {
            "LENGTH":0,
            "UNPREDICTIBILITY":0,
            "COMPLEXITY":0
        }
        result["LENGTH"] = (len(password) if len(password) <= 10 else 10)

        # CHECK 2
        track = []
        dupes = 0
        for char in password:
            
            if char in track:
                dupes += 1
                continue

            track.append(char)
        result["UNPREDICTIBILITY"] = (10-dupes if dupes <= 10 else 0)
        results[password] = result

        # CHECK 3
        UPPER = 0
        LOWER = 0
        NUMS = 0
        SYMS = 0
        for char in password:
            if char in chars["UPPER"]:
                UPPER += 1
            elif char in chars["LOWER"]:
                LOWER += 1
            elif char in chars["NUMBERS"]:
                NUMS +=1
            elif char in chars["SYMBOLS"]:
                SYMS += 1

        AVERAGE = (UPPER+LOWER+NUMS+SYMS)/4
        MAX = max([UPPER, LOWER, NUMS, SYMS])
        result["COMPLEXITY"] = (round((AVERAGE/MAX)*10, 1))

    # GOAL 2
    final = []
    for key, values in results.items():
        final.append(key)
        for criteria, score in values.items():
            final.append(f"{criteria}: {score}/10")
        final.append(" ")

    return "\n".join(final)