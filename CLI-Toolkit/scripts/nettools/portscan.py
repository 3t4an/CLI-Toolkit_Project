import socket
def portscan(args):
    try:
        IP = args["-ip"]
        IP = IP.split(".")
        IP = [x for x in IP if x.isdigit() == True and int(x) <= 255 and int(x) >= 0]
        if len(IP) != 4:
            return f"Bad Argument: {args['-ip']}"
        IP = ".".join(IP)

        print(f"PORT RESULTS: {IP}")
        COUNT = 0
        for PORT in range(int(args["-start"]), int(args["-end"])+1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)

            result = s.connect_ex((IP, PORT))

            if result == 0:
                print(f"\033[32m{PORT} : OPEN\033[39m")
                COUNT += 1
            else:
                print(f"\033[31m{PORT} : CLOSED\033[39m")
            
            s.close()
        return f"{COUNT}/{(int(args['-end'])+1)-int(args['-start'])}"
    except KeyboardInterrupt:
        return "Control-C"