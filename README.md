# CLI-Toolkit_Project

## DISCLAIMER
This project is intended for educational and/or authorized testing purposes only. Do not use it on systems or networks without permission.

## DESCRIPTION
This project has multiple password and network based tools which can be run directly from the Windows Command Prompt. This project was intented to restart my programming journey after being busy with school for a while. Initially, the project as supposed to be separate from the Windows command prompt; but then, I shifted the trajectory and made it a runnable variaty of tools directly from the Windows Command Prompt.

## PROJECT DIRECTORY
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

## HOW TO TYPE COMMANDS:
Commands are broken down into 3 sections.
(toolname) (mode) (args)

Arguments are put in a very strict flag:value structure.
-flag value

Tools without multiple modes can be put as default or left blank.

Example Commands:
portscan default -ip 0.0.0.0 -start 80 -end 100

hashx -pass test_pass -hash SHA1

## INSTALLATION PROCCESS
1. Extract .zip file of the CLI-Toolkit Project into desired directory
2. Copy the directory of the folder know as 'batch'
4. Type, 'Edit the system environment variables', this should open up the Control Panel
5. Look to the bottom-right, click, 'Environment Variables...'
6. At the bottom of the new window, find, 'System variables'
7. Use the scroll wheel to find, 'path', in this 'System Variables' section.
8. Double-Click on 'path'
9. Locate, 'New' in the new window and click on it.
10. Paste the copied directory of the folder known as, 'batch'
11. Click 'OK', on everything to exit.
12. NOW YOU CAN RUN THE PROJECT COMMANDS FROM THE WINDOWS COMMAND PROMPT!

## PROJECT COMMANDS:
passgen - allows users to create a personalized password wordlist or create a strong randomized password
passguard - rates the password provided by the user
hashx - hashes the provided password using a speicfied hash
netscan - pings all IPs in the local network using the specified range and amount of ICMP requests
portscan - scans the ports of a specified IP on the local network using the range provided.

## REQUIREMENTS:
python 3.11.9+
Windows
