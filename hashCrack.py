"""
File:          hashCrack.py
Description:   This program cracks passwords using a custom dictionary wordlist if a SHA1
               hash of a leaked password is provided.
"""


import hashlib
import argparse

# command line arguments
parser = argparse.ArgumentParser(description="SHA1 Cracker")
# adding hashtype argument, required to run
parser.add_argument("-sha1", dest="hash", help="sha1 hash", required=True)
# adding dictionary argument, required to run
parser.add_argument("-w", dest="wordlist", help="wordlist", required=True)
# parse the arguments
parsed_args = parser.parse_args()

def main(): 
    hash_cracked = "" # empty string for hash not cracked
    with open(parsed_args.wordlist) as file:
        # open wordlist file and go line by line
        for line in file:
            # strip whitespaces from the string
            line = line.strip()
            # this is were the conversion and comparison of SHA1 hash occurs
            if hashlib.sha1(bytes(line,encoding="utf-8")).hexdigest() == parsed_args.hash:
                hash_cracked = line
                print("\nThe Password for the SHA1 HASH is %s."%line)
    if hash_cracked == "":
        print("\nCan't crack the HASH. Try a different dictionary.")

if __name__ == "__main__":
    main()
