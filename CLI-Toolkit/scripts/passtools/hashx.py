import hashlib

def hashx(args):
    hashes = list(hashlib.algorithms_guaranteed)

    # if -hash is unknown - defaults to SHA1
    if args["-hash"][0] not in hashes:
        args["-hash"][0] = "SHA1"
        print("hashx default to hash SHA1")

    results = ""

    hash = hashlib.new(args["-hash"][0])

    for password in args["-pass"]:
        hash.update(password.encode())
        hashed_password = hash.hexdigest()
        results = results+f"{password}\n{hashed_password}\n"
    
    return results