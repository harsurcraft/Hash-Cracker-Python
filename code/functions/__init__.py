# The name of God

# Importing:
import functions.intro
import functions.outro
import functions.hash
from functions import variables as var
import hashlib

# Class:

# This class has the mian code
class Cracker:
    """This class, is the main code:
    The code of intro, hashing, inputs and etc is in it."""
    
    def __init__(self) -> None:     
        self.Modes = var.HMD()
        
    # This function print the intro and inputs   
    def Intro(self) -> None:
        """This function, 
        print the intro(logo and help message)"""
        
        # Intro printing:
        functions.intro.intro()
        
    def Crack(self) -> str:
        """This function start cracking the hash and do some inputs like:(
        hashed word, loction of wordlist, type of hashing modes). """
        
        # Variables:
        Hash = functions.hash.hashed_text()
        hash_type = functions.hash.chose(self.Modes)
        is_tlocation = False
        unhashed = None
        
        while not is_tlocation:
            
            try:
                # Inputing the wordlist
                # then saving that in a var:
                wordlist_location = input("[Py]-$ Enter the location of wordlist : \
                                            \n warrning : (if it dos'nt work you move the wordlist to the code folder, \
                                            \n then you enter the file name) : ")

                with open(wordlist_location, "r") as wordlist_opened:
                    wordlist = (wordlist_opened.read()).split()
                    
                is_tlocation = True

            except:
                # Warnning:
                print()
                print("_________________________")
                print()
                print("[Py]-$ Please Enter check the enter location or file name!!")
                print("_________________________")
                print()     

        
        for word in wordlist:
            
            word_encoded = word.encode() 
            
            # Checking the chose of user
            # then hash the words 
            # with chosed type:
            match hash_type:
                case 0:
                    # Creating a hash word:
                    hashed = []
                    hashed.append(hashlib.md5(word_encoded).hexdigest())
                    hashed.append(hashlib.sha1(word_encoded).hexdigest())
                    hashed.append(hashlib.sha224(word_encoded).hexdigest())
                    hashed.append(hashlib.sha256(word_encoded).hexdigest())
                    hashed.append(hashlib.sha512(word_encoded).hexdigest())
                    hashed.append(hashlib.sha384(word_encoded).hexdigest())
                    hashed.append(hashlib.sha3_256(word_encoded).hexdigest())
                    hashed.append(hashlib.sha3_224(word_encoded).hexdigest())
                    hashed.append(hashlib.sha3_384(word_encoded).hexdigest())
                    hashed.append(hashlib.sha3_512(word_encoded).hexdigest())
                    hashed.append(hashlib.blake2s(word_encoded).hexdigest())
                    hashed.append(hashlib.blake2b(word_encoded).hexdigest())

                    # Cheking all of the hashes:
                    for i in range(len(hashed)):
                        if Hash == hashed[i]:
                            # Printting the word
                            # then exit the app:
                            unhashed = word

                case 1:
                    hashed = hashlib.md5(word_encoded).hexdigest()
                    if hashed == Hash:
                        # Printting the word
                        # then exit the app:
                        unhashed = word

                case 2:
                    # Creating a hash word:
                    hashed = hashlib.sha1(word_encoded).hexdigest()
                    # Cheking the hashed word is the hashed of secret code::
                    if hashed == Hash:
                        # Printting the word
                        # then exit the app:
                        unhashed = word

                        
                case 3:
                    # Creating a hash word:
                    hashed = hashlib.sha224(word_encoded).hexdigest()

                    # Cheking the hashed word is the hashed of secret code::
                    if hashed == Hash:
                        # Printting the word
                        # then exit the app:
                        unhashed = word

                case 4:
                    # Creating a hash word:
                    hashed = hashlib.sha256(word_encoded).hexdigest()

                    # Cheking the hashed word is the hashed of secret code::
                    if hashed == Hash:
                        # Printting the word
                        # then exit the app:
                        unhashed = word

                case 5:
                    # Creating a hash word:
                    hashed = hashlib.sha512(word_encoded).hexdigest()

                    # Cheking the hashed word is the hashed of secret code::
                    if hashed == Hash:
                        # Printting the word
                        # then exit the app:
                        unhashed = word

                case 6:
                    # Creating a hash word:
                    hashed = hashlib.sha384(word_encoded).hexdigest()

                    # Cheking the hashed word is the hashed of secret code::
                    if hashed == Hash:
                        # Printting the word
                        # then exit the app:
                        unhashed = word

                case 7:
                    # Creating a hash word:
                    hashed = hashlib.sha3_256(word_encoded).hexdigest()

                    # Cheking the hashed word is the hashed of secret code::
                    if hashed == Hash:
                        # Printting the word
                        # then exit the app:
                        unhashed = word

                case 8:
                    # Creating a hash word:
                    hashed = hashlib.sha3_224(word_encoded).hexdigest()

                    # Cheking the hashed word is the hashed of secret code::
                    if hashed == Hash:
                        # Printting the word
                        # then exit the app:
                        unhashed = word

                case 9:            
                    # Creating a hash word:
                    hashed = hashlib.sha3_384(word_encoded).hexdigest()

                    # Cheking the hashed word is the hashed of secret code::
                    if hashed == Hash:
                        # Printting the word
                        # then exit the app:
                        unhashed = word

                case 10:
                    # Creating a hash word:
                    hashed = hashlib.sha3_512(word_encoded).hexdigest()

                    # Cheking the hashed word is the hashed of secret code::
                    if hashed == Hash:     
                        # Printting the word
                        # then exit the app:
                        unhashed = word

                case 11:            
                    # Creating a hash word:
                    hashed = hashlib.blake2s(word_encoded).hexdigest()

                    # Cheking the hashed word is the hashed of secret code::
                    if hashed == Hash:
                        # Printting the word
                        # then exit the app:
                        unhashed = word
     
                case 12:
                    # Creating a hash word:
                    hashed = hashlib.blake2b(word_encoded).hexdigest()

                    # Cheking the hashed word is the hashed of secret code::
                    if hashed == Hash:
                        # Printting the word
                        # then exit the app:
                        unhashed = word
                        
        if unhashed == None:
                print()
                print("______________________________________________")
                print()
                print("[Py]-$ Detecting the hashing type .....")
                print()
                print("[Py]-$ The word Not Found")
                print()
                print("______________________________________________")
                
                return None    # Returning the word Not Found     
        else:           
            return unhashed
                     
    def Outro(self, word: str) -> None:
        """This function check if the word founded or not founded do some codes"""
        
        if not word == None:
            functions.outro.outro(word)
        else:
            print()
        