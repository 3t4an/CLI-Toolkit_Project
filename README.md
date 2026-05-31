# CLI-Toolkit_Project

## DISCLAIMER
This project is intended for educational and/or authorized testing purposes only. Do not use it on systems or networks without permission.

## Description
This project has multiple password and network based tools which can be run directly from the Windows Command Prompt.

## Why I Built This
This project was intented to restart my programming journey after being busy with school for a while. Initially, the project as supposed to be separate from the Windows Command prompt; but then, I shifted the trajectory and made it a runnable variaty of tools directly from the Windows Command Prompt.

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

## Setup after Installation
1. Extract .zip file of the CLI-Toolkit Project into desired directory.
2. Run, '**install_dependencies.bat**' to install the neccessary python libraries.
3. Copy the directory of the folder know as '**batch**'.
4. Type, '**Edit the system environment variables**', into the Windows Search, this should open up the Control Panel.
5. Look to the bottom-righta and click, '**Environment Variables...**'.
6. At the bottom of the new window, find, '**System variables**'.
7. Use the scroll wheel to find, '**path**', in this '**System Variables**' section.
8. Double-Click on '**path**'.
9. Locate, '**New**' in the new window and click on it.
10. Paste the copied directory of the folder known as, '**batch**'
11. Click '**OK**', on everything to exit.

You can now run any of the CLI-Toolkit command from any directory in the Windows Command Prompt

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

## Reference:
|  Toolname  |  Description
| :--------- | :-----------
| passgen    | allows users to create a personalized password wordlist or create a strong randomized password
| passguard  | rates the password provided by the user
| hashx      | hashes the provided password using a speicfied hash
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
