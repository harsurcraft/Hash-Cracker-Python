# بسم الله الرحمن الرحیم
# ____________________________________________________________________________________________
# This app unhash, lots of hashes :
# You can use this app to unhash a password some times it diden't work
# Then you can crack the seceret code with this app
# _____________________________________________________________________________________________________
# By MR.Harsurcraft
#
# __________codes__________
#

# Importing:
import hashlib
from functions import *

# Functions:
def crak() -> None:
    cracker_EX = Cracker()
    cracker_EX.Intro()
    word = cracker_EX.Crack()
    cracker_EX.Outro(word=word)


# Vars:
running = True


if __name__ == "__main__":
    crak()
    
    while running:
        runnig_stutus = input("[Py]-$ Do you whant to continue, ? [Y/N/any thing else = yes] (Defult = Y) : ")
    
        match runnig_stutus:
            case "Y":
                crak()
            case "N":
                exit()
            case _ :
                crak()
    