# CLI-Toolkit_Project

## DISCLAIMER
This project is intended for educational and/or authorized testing purposes only. Do not use it on systems or networks without permission.

## Summary
The CLI-Toolkit Project is a variety of network and password based commands that can be run from the Windows Command Prompt

## Goals
When building, I was trying to achieve an easier way to run cybersecurity commands from the CMD without needing to open another tool. This project was also intended to restart my programming and cybersecurity journey after being busy with school for a while.

## Steps Taken to Build
1. Planning - Spent a few weeks mapping out how would build the project and timeline that would be used to execute it.
2. Starting Building - I first designed the `main.py` which would be the center of all commands and handled command parsing, checking and interpretation.
3. Tool Building - After programming `main.py`, I began building the tools in this order:<br>
  a. `wordforge.py`<br>
  b. `securegen.py`<br>
  c. `passguard.py`<br>
  d. `hashx.py`<br>
  e. `ping.py`<br>
  f. `netscan.py`<br>
  g. `portscan.py`<br>
4. Intention Change - I realized that for the tools to work coherently, they would need Windows commands like `ping` and `arp`. However after building `ping.py`, I had the bright idea of making the project integrated with the Windows Command Prompt. This way, users could utilize the tools really easily while also having access to Windows own networking tools. This transition fulfilled one of the major goals.
5. Make `interpreter.py` - After rebuilding a new plan, I began by changing `main.py` to `interpreter.py`. This change would allow arguments to be passed through the Python script, interpreted, and passed on to the right command.
6. Create `.bat`'s - For the commands to be properly passed through from the CMD to `interpreter.py`, it needed a bridge. The batch files for each command successfully convey the passed arguments to `interpreter.py`.
7. Create `help.py` - Like the CMD commands, I developed a `-h` tag for each command to see the proper usage.
8. Debug & Publish to GitHub - After rebuilding the project, debugging each tool, fixing errors and testing, I created **my first GitHub Repo**

## Basic Usage:
Commands are broken down into 3 sections.
(toolname) (mode) (args)

Arguments are put in a very strict flag:value structure:
`-ip 0.0.0.0`

Tools without multiple modes can be put as default or left blank:<br>
`hashx default -pass test_pass -hash SHA1`<br>
v<br>
`hashx -pass test_pass -hash SHA1`

Example Commands:<br>
`portscan default -ip 0.0.0.0 -start 80 -end 100`<br>
`passgen wordlist -file testing -first test -last user -month 01 -day 01`

## Demo
```cmd
C:\Users\demo>hashx -pass 1234 -hash sha1
1234
7110eda4d09e062aa5e4a390b0a572ac0d2c0220

C:\Users\demo>passgen securegen -length 10 -remove upper,symbols
et9m3k5xbl
```

## Setup after Installation
1. Extract .zip file of the CLI-Toolkit Project into desired directory
2. Copy the directory of the folder know as '**batch**'.
3. Type, '**Edit the system environment variables**', into the Windows Search, this should open up the Control Panel.
4. Look to the bottom-right and click, '**Environment Variables...**'.
5. At the bottom of the new window, find, '**System variables**'.
6. Use the scroll wheel to find, '**path**', in this '**System Variables**' section.
7. Double-Click on '**path**'.
8. Locate, '**New**' in the new window and click on it.
9. Paste the copied directory of the folder known as, '**batch**'
10. Click '**OK**', on everything to exit.

You can now run any of the CLI-Toolkit command from any directory in the Windows Command Prompt

## Tools Used
The CLI-Toolkit Project utilizes many of Python's various built-in libraries:
1. sys - for exiting the script when errors occur
2. os - for directory handling
3. itertools - for combination building in `wordforge.py`
4. random - for creating a strong, randomized password in `securegen.py`
5. hashlib - for hashing input using the desired hash in `hashx.py`
6. socket - for interacting with ports in `portscan.py`
7. subprocess - for pinging local network IPs in `netscan.py`

## What did I learn
I learned that for scripts which take raw input from users, I should constantly test and find common mistakes that people might make. Computers are dumb, and it is necessary for the script to handle all types of input from the users to aviod failure and errors being thrown. This is an essential skill to learn for many entry-level jobs. When building scripts that scan or take in information, it is necessary for the script to be prepared to handle all types of information being thrown at it. I also discovered how easy it is to integrate scripts with the Windows Command Prompt. Meaning, building custom commands and allowing custom tools to be run. This makes it much easier for a developer or user to access complex commands not built-in to Windows. 

## What should I build next?
With my recent planning to get into Cybersecurity and transition my Python learning to be more security-based, I leaning toward a Log Scanner. This mini project is intended to use my Python fundamentals and curved it toward security. This is a crucial part in my three-step roadmap to fully integrate my Cybersecurity journey with my Python journey.


## Project Directory
```
CLI-Toolkit/
│
├── interpreter.py
├── main.py
│
├── scripts/
│   ├── nettools/
│   |     ├── netscan.py
│   |     ├── portscan.py
│   ├── passtools/
│   |     ├── wordforge.py
│   |     ├── securegen.py
│   |     ├── passguard.py
│   |     ├── hashx.py
├── batch/
│   ├── wordforge.bat
│   ├── securegen.bat
│   ├── passguard.bat
│   ├── hashx.bat
│   ├── netscan.bat
│   ├── portscan.bat
```

## Reference:
|  Toolname  |  Description
| :--------- | :-----------
| passgen    | allows users to create a personalized password wordlist or create a strong randomized password
| passguard  | rates the password provided by the user
| hashx      | hashes the provided password using a specified hash
| netscan    | pings all IPs in the local network using the specified range and amount of ICMP requests
| portscan   | scans the ports of a specified IP on the local network using the range provided.

| Other  | Command Example | Notes
| :----- | :-------------- | :-------
| `-h`   | `passgen -h`    | Shows the help menu for the command from the [help.py](https://github.com/3t4an/CLI-Toolkit_Project/blob/main/CLI-Toolkit/help.py)
| `,`    | `passgen wordforge -file test -first test,testing` | Used to separate multiple values for a single flag

## Licence
Licensed under the [Apache 2.0](https://github.com/3t4an/CLI-Toolkit_Project/blob/main/LICENSE) Licence

## REQUIREMENTS:
python 3.11.9+<br>
Windows
