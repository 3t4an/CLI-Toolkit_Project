import sys
from scripts.passtools.wordforge import wordforge
from scripts.passtools.securegen import securegen
from scripts.passtools.passguard import passguard
from scripts.passtools.hashx import hashx
from scripts.nettools.netscan import netscan
from scripts.nettools.portscan import portscan
from help import passgen_help
from help import passguard_help
from help import hashx_help
from help import netscan_help
from help import portscan_help
import os

# MAIN LOOP HELPER FUNCTIONS
def parse_keys(commands):

    # GOALS:
    # 1. Parse raw code into key:values (readable for functionality)
    # 2. Duplicate keys -> Error
    # 3. Orphan values (no key) -> Error

    commands = commands[2:]
    args = {}
    flag = None

    for command in commands:
        if command[0] == "-":
            # DUPLICATE FLAGS        
            if command in args:
                return [False, f"Duplicate of '\033[31m{command}\033[39m' found"]
            
            # ORPHAN FLAGS
            if flag:
                return [False, f"Flag '\033[31m{flag}\033[39m' requires more than 0 arguments"]
            flag = command
            args[flag] = None
        else:
            # ORPHAN VALUES
            if flag != None:
                args[flag] = command
                flag = None
            else:
                return [False, error(command)]
    
    # ORPHAN FLAG AT END
    if args:
        last_value = args[list(args.keys())[-1]]
        if last_value is None:
            return [False, f"Flag '\033[31m{list(args.keys())[-1]}\033[39m' requires more than 0 arguments"]
        

    # results in something like {"-pass": 1234, "-user":"person"}
    return [True, args]

def check_mode(toolname, mode):
    # GOALS
    # 1. Make sure mode exists for tool
    # 2. Deciding fallback behavior

    if mode in TOOL_KEYS[toolname]:
        return [True, mode]
    else:
        return [False, error(mode)]

def check_keys(toolname, mode, keys):

    # GOALS
    # 1. Make sure there are only allowed keys
    # 2. Make sure required keys are present

    REQUIRED = TOOL_KEYS[toolname][mode]["required"]
    OPTIONAL = TOOL_KEYS[toolname][mode]["optional"]

    # CHECK #1
    for key in keys:
        if key not in REQUIRED and key not in OPTIONAL:
            return ["EX", error(key)]
    
    # CHECK #2
    for key in REQUIRED:
        if key not in keys:
            return ["REQ", f"Required key '{key}' not found"]

    return [None, None]

def error(word):
    return f"Command '\033[31m{word}\033[39m' not recognized"
TOOL_KEYS = {
    "passgen":{
        "wordforge":{
            "required":["-file"],
            "optional":["-first", "-last", "-role", "-username", "-year", "-month", "-day", "-other", "-omit"]
        },
        "securegen":{
            "required":["-length"],
            "optional":["-remove", "-file"]
        },
        "-h":{
            "required":[],
            "optional":[]
        }
    },
    "passguard":{
        "default":{
            "required":["-pass"],
            "optional":[]
        },
        "-h":{
            "required":[],
            "optional":[]
        }
    },
    "hashx":{
        "default":{
            "required":["-pass", "-hash"],
            "optional":[]
        },
        "-h":{
            "required":[],
            "optional":[]
        }
    },
    "netscan":{
        "default":{
            "required":["-count", "-start", "-end"],
            "optional":[]
        },
        "-h":{
            "required":[],
            "optional":[]
        }
    },
    "portscan":{
        "default":{
            "required":["-ip", "-start", "-end"],
            "optional":[],
        },
        "-h":{
            "required":[],
            "optional":[]
        }
    }
}

# BEGINNING LOOP
# --------------------COMMAND INTERPRETATION PROCESS-----------
# 1. Parse Command (check command formatting/make suitable for use)
# 2. Parse Mode (check mode)
# 3. Parse Keys (check keys formatting)
# 4. Check Keys (check keys per tool/mode)
# 5. Execute
# -------------------------------------------------------------

# PARSE COMMAND e.g (["auth", "login", "-user", "-pass"])
command = sys.argv[1].split(" ")
command = [x for x in command if x != ""]
if len(command) == 0:
    sys.exit()

# for cases that don't exist
if command[0] not in TOOL_KEYS:
    print(error(command[0]))
    sys.exit()

# for cases without specified mode: default
if len(command) > 2 and "-" in command[1] and "default" in TOOL_KEYS[command[0]]:
    command.insert(1, "default")

# for cases present with nothing but itself (auth)
if len(command) == 1:
    print(error("mode"))
    sys.exit()

# PARSE MODE
mode = check_mode(command[0], command[1])
if mode[0] == True:
    mode = mode[1]
else:
    print(mode[1])
    sys.exit()

# PARSE KEYS e.g. (-user, -pass)
result = parse_keys(command)
if result[0] == False:
    print(result[1])
    sys.exit()
elif result[0] == True:
    keys = result[1]

# CHECK KEYS
result = check_keys(command[0], mode, keys)
if result[0] == "EX":
    print(result[1])
    sys.exit()
elif result[0] == "REQ":
    print(result[1])
    sys.exit()

    
if command[0] == "passgen" and mode == "wordforge":

    if "," in keys["-file"]:
        print("Flag \033[31m'-file'\033[39m takes only one argument")
        sys.exit()

    args = {}

    for key, value in keys.items():
        value = value.split(",")
        args[key] = value
    
    print(wordforge(args))
    sys.exit()
elif command[0] == "passgen" and mode == "securegen":

    if "," in keys["-length"]:
        print("Flag \033[39m'-length'\033[31m takes only one argument")
    elif not keys["-length"][0].isdigit():
        print("Flag \033[31m'-length'\033[39m must be integer")
    elif keys["-length"][0] == "0":
        print("Length of password \033[31mcannot be zero\033[39m")
    elif "-file" in keys and "," in keys["-file"]:
        print("Flag \033[31m'-file'\033[39m takes only one argument")

    args = {}

    for key, value in keys.items():
        value = value.split(",")
        args[key] = value
    
    print(securegen(args))
    sys.exit()

elif command[0] == "passgen" and mode == "-h":
    print(passgen_help())

elif command[0] == "passguard" and mode == "default":

    args = {}
    for key, value in keys.items():
        value = value.split(",")
        args[key] = value
    
    print(passguard(args))
    sys.exit()

elif command[0] == "passguard" and mode == "-h":
    print(passguard_help())

elif command[0] == "hashx" and mode == "default":
    
    if "," in keys["-hash"]:
        print("Flag \033[31m'-hash'\033[39m takes only one argument.")
        sys.exit()

    args = {}
    for key, value in keys.items():
        value = value.split(",")
        args[key] = value
    
    print(hashx(args))
    sys.exit()

elif command[0] == "hashx" and mode == "-h":
    print(hashx_help())

elif command[0] == "netscan" and mode == "default":

    args = {}

    for key, value in keys.items():
        if "," in value:
            print(f"Flag \033[31m'-{key}'\033[39m takes only one argument.")
        sys.exit()
        args[key] = int(value)

    if not args["-end"].isdigit() or not args["-start"].isdigit():
        print("Flag \033[31m'-end' \033[39mand\033[31m '-start'\033[39m must be integer.")
        sys.exit()
    elif int(args["-start"]) > int(args["-end"]):
        print("Flag \033[31m'-start'\033[39m cannot be larger than flag \033[31m'-end'\033[39m")
        sys.exit()
    
    print(netscan(args))

elif command[0] == "netscan" and mode == "-h":
    print(netscan_help())

elif command[0] == "portscan" and mode == "default":

    args = {}
    
    for key, value in keys.items():
        if "," in value:
            print(f"Flag \033[31m'-{key}'\033[39m takes only one argument.")
            sys.exit()
        args[key] = value
    
    if not args["-end"].isdigit() or not args["-start"].isdigit():
        print("Flag \033[31m'-end' \033[39mand\033[31m '-start'\033[39m must be integer.")
        sys.exit()
    elif int(args["-start"]) > int(args["-end"]):
        print("Flag \033[31m'-start'\033[39m cannot be larger than flag \033[31m'-end'\033[39m")
        sys.exit()
    
    print(portscan(args))

elif command[0] == "portscan" and mode == "-h":
    print(portscan_help())