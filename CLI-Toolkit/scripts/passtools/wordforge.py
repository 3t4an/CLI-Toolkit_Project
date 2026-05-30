import itertools
import os

def wordforge(args):
    if len(args.keys()) == 1:
        return ""

    if "-omit" in args:
        OMIT = args.pop("-omit")
        OMIT = ["-"+x for x in OMIT]
    else:
        OMIT = []

    if "-leet" in args:
        LEET = args.pop("-leet")
        LEET = ["-"+x for x in LEET]
    else:
        LEET = []
    FILE = args.pop("-file")[0]

    def variants(key, value):
        value = str(value)
        if (key == "-month" or key == "-day") and key.isdigit():
            return [value]
        elif key == "-year":
            return ([value, value[-2:]] if len(value) >= 3 and value.isdigit() else [value])

        vars = [value.upper(), value.lower(), value.title()]

        if key in OMIT:
            vars.append("")

        if key == "-first" or key == "-last":
            vars.append(value[0].lower())
            vars.append(value[0].upper())
        
        return vars

    # STEP ONE:
    new_args = {}
    for key, values in args.items():
        new_values = []
        for value in values:
            var = variants(key, value)
            new_values.append(var)
        new_args.update({key: new_values})
    
    # STEP TWO:
    flat = [[item for sublist in values for item in sublist] for values in new_args.values()]

    # STEP THREE
    LENGTH = len(flat)
    new_flat = []
    for i in range(LENGTH):
        new_flat.append(flat[i])
        new_flat.append(["-", "_", ""])
    new_flat.pop(-1)

    # STEP FOUR:
    DIR = os.path.dirname(os.path.abspath(__file__))
    DIR = os.path.dirname(DIR)
    DIR = os.path.dirname(DIR)
    DIR = os.path.join(DIR, "data")
    print(DIR)
    result = []
    with open(f"{DIR}\{FILE}.txt", "w") as file:
        for combo in itertools.product(*new_flat):
            file.write(f"{''.join(combo)}\n")
            result.append(f"{''.join(combo)}\n")
    return "\n".join(result)