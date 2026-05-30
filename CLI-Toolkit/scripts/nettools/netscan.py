import subprocess as sp

def netscan(args):

    START = args["-start"]
    END = args["-end"]
    COUNT = args["-count"]

    # GET NETWORK PREFIX
    IP = sp.run(
        ["ipconfig"],
        capture_output=True,
        text=True
    )
    IP = IP.stdout.splitlines()
    for line in IP:
        if "IPv4" in line:
            ip_address = line.split(":")[1].strip()
            NETWORK_IDENTIFIER = ".".join(ip_address.split(".")[0:3])
            break
    TOTAL = (END+1)-START
    SUCCESS = 0

    for i in range(START, END+1):
        IP = f"{NETWORK_IDENTIFIER}.{i}"
        COMMAND = f"ping -n {COUNT} {IP}".split(" ")
        result = sp.run(
            COMMAND
        )
        if result.returncode == 0:
            print(f"\033[32mSUCCESS PINGING: {IP}\033[39m")
            SUCCESS += 1
        else:
            print(f"\033[31mFAILURE PINGING: {IP}\033[39m")
    
    return f"\033[34m{SUCCESS}/{TOTAL}\033[39m"