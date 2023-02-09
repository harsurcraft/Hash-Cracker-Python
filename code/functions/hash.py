# In the name of Allah(God)

def chose(hashing_mode: list[str]) -> int : # type: ignore
    """
    This function, print the hash modes
    we got and then, 
    get the type of the hashing mode
    Then if the user chose out of
    the typs it send a message
    """
        
    print()
    print("[0]", hashing_mode[0])
    print("[1]", hashing_mode[1])
    print("[2]", hashing_mode[2])
    print("[3]", hashing_mode[3])
    print("[4]", hashing_mode[4])
    print("[5]", hashing_mode[5])
    print("[6]", hashing_mode[6])
    print("[7]", hashing_mode[7])
    print("[8]", hashing_mode[8])
    print("[9]", hashing_mode[9])
    print("[10]", hashing_mode[10])
    print("[11]", hashing_mode[11])
    print("[12]", hashing_mode[12])
    print()
    print("_________________________________________")
    print()
    
    # Hashing type and checking the enter type:
    Enter_int = False
    while not Enter_int:
        # This while get the type of hashing and check it if it isn't True it back and do all of this progres
        
        try:
            Enter = int(input("[Py]-$ Chose one code : "))
            
            if 0 <= Enter <= 11: 
                Enter_int = True
            else:
                Enter_int = False
        
        # if the Enter code isn't int do this        
        except:
            # Warnning:
            print()
            print("_________________________")
            print("")
            print("[Py]-$ Please enter a number!!")
            print("_________________________")
            print()     
    

    match Enter:
        case 0:
            return 0
        case 1:
            return 1
        case 2:
            return 2
        case 3:
            return 3
        case 4:
            return 4
        case 5:
            return 5
        case 6:
            return 6
        case 7:
            return 7
        case 8:
            return 8
        case 9:
            return 9
        case 10:
            return 10
        case 11:
            return 11

def hashed_text() -> str: 
    """This function, 
    get the hashed text, 
    the return that"""
    
    return str(input("[Py]-$ Enter the hashed text : "))
