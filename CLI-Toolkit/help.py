def passgen_help():
    results = '''
*usage provides no particular order*

Usage: passgen wordforge [-file] [-first] [-last] [-role] [-username] [-year]
                         [-month] [-day] [-other] [-omit]

       passgen securegen [-length] [-remove] [-file]

Options:
    wordforge
        DESCRIPTION:
        This tool (passgen wordforge), creates a password wordlist of potential
        passwords with the given arguments. Password format will be based on flag
        placement order within the command.

        REQUIRED FLAGS:
        -file       Specify the name of the output file.

        OPTIONAL FLAGS:
        -first      Specify a potential first name to be included.
        -last       Specify a potential last name to be included.
        -role       Specify a potential role to be included.
        -username   Specify a potential username to be included.
        -year       Specify a potential related year to be included.
        -month      Specify a potential related month to be included.
        -day        Specify a potential related day to be included.
        -omit       Omit a certain argument to be blank in some iterations.
        -other      Specify a potential attribute not listed in flag to be included.
    
    securegen
        DECRIPTION:
        This tool (passgen securegen), creates a randomized password based on the
        arguments provided.

        REQUIRED FLAGS:  
        -length     Specify the length of the desired password

        OPTIONAL FLAGS:
        -remove     Specify a potential type of character to be removed (lower,upper,numbers,symbols)
        -file       Specify the potential name of the output file.
    
    -h
        Provides Usage about command: passgen
'''
    return results

def passguard_help():
    results = '''
*usage provides no particular order*
*default is not needed to be included in the command*

Usage: passguard default [-pass]

Options:
    default
        DESCRIPTION:
        This tool (passguard), take in a password a rates it out of ten based on
        LENGTH, UNPREDICTIBILIY, and COMPLEXITY.

        LENGTH - the ideal length is 10 characters or more.
        UNPREDICTIBLITY - is rated based on the amount of duplicates in a password.
        COMPLEXITY - is rated on the variety of characters used (UPPER - LOWER - NUMS - SYMS).

        REQUIRED FLAGS:
        -pass       Give the selected password to rate.

        OPTIONAL FLAGS:
    
    -h
        Provides Usage about command: passguard
'''
    return results

def hashx_help():
    results = '''
*usage provides no particular order*
*default is not needed to be included in the command*

Usage: hashx default [-pass] [-hash]

Options:
    default
        DESCRIPTION:
        This tool (hashx), takes a password and hashes it based using the
        provided hash.

        REQUIRED FLAGS:
        -pass       Give the selected password to hash.
        -hash       Give the selected hash to hash the password with:
                    sha384, sha3_224, blake2s, shake_256, md5, sha256, sha224, 
                    sha3_384, shake_128, blake2b, sha3_512, sha512, sha3_256, sha1
                    ANY HASH THAT IS NOT RECOGNIZE WILL DEFAULT TO sha1

        OPTIONAL FLAGS:
    
    -h
        Provides Usage about command: hashx
'''
    return results

def netscan_help():
    results = '''
*default is not needed to be included in the command*

Usage: netscan default [-count] [-start] [-end]

Options:
    default
        DESCRIPTION:
        This tool (netscan), pings each potential ip in a local network using a start
        host section and end host section: (-start 1 -end 5 -> 192.168.72.1 - 192.16872.5)

        REQUIRED FLAGS:
        -count      Give the amount of packages to ping each potential host with.
        -start      Give the beginning host section of the ip
        -end        Give the end host section of the ip

        OPTIONAL FLAGS:
    
    -h
        Provides Usage about command: netscan
'''
    return results

def portscan_help():
    results = '''
*default is not needed to be included in the command*

Usage: portscan default [-ip] [-start] [-end]

Options:
    default
        DESCRIPTION:
        This tool (portscan), scans each port of the targeted ip from -start to
        -end.

        REQUIRED FLAGS:
        -ip         Give the target ip address
        -start      Give the start port of the target ip to be scanned
        -end        Give the end port of the target ip to be scanned

        OPTIONAL FLAGS:
    
    -h
        Provides Usage about command: portscan
'''
    return results