#CRACKSHA256a
#Filip Rokita
#www.filiprokita.com

import hashlib

hash = input("SHA256: ")
wordlist = input("WORDLIST: ")
cracked = 0

try:
    openedWordlist = open(wordlist, "r")
except:
    print("Wordlist does not exist!")
    input()
    quit()

for word in openedWordlist:
    encodedWord = word.encode()
    tryingNow = hashlib.sha256(encodedWord.strip()).hexdigest()
    if tryingNow == hash:
        print("\n")
        print("HASH CRACKED: ", word)
        print("\n")
        cracked = 1
        input()
        quit()

if cracked == 0:
    print("Correct word does not exist in wordlist!")
    input()
    quit()