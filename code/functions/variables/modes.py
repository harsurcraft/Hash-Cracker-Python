# The name of God

# Function:

# It will return a list of modes:
def modes() -> list[str]:
    """This function, 
    return a list of hashing types we can do in this Program"""
    
    # Modes
    hash_modes = [
        "all", "md5","sha1", "sha224",
        "sha256", "sha512", "sha384",
        "sha3_256","sha3_224", "sha3_384",
        "sha3_512","blake2s", "blake2b", 
        ]
    
    return hash_modes