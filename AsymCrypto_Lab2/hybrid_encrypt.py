from cryptography.hazmat.primitives.asymmetric import rsa
import sys,os
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from random import random

from  cryptography.hazmat.primitives.ciphers import Cipher,algorithms,modes

# ===============WIP====================
def hybrid_encrypt(public_key,message,outfile):
    if sys.getsizeof(message)>public_key.key_size:
        print("Object too large, doing hybrid cipher")
        key=os.urandom(public_key.key_size-random.randint(1,20))
        
if __name__== "__main__":
    if len(sys.argv)<4:
        print("ERROR\nUsage:\n python3 rsa_encrypt.py <key>  -m OR -f <file_to_encrypt>\n-m -- read from commandline \nf -- read from file\nGood luck and thanks for all the fish!")
        exit(1)
    key_file = sys.argv[1]
    option = sys.argv[2]
    content = sys.argv[3]
    if len(sys.argv) == 5:
        outfile = sys.argv[4]
    else:
        outfile = "cryptogram.bin"
    try:
        with open(key_file, "rb") as f:
            key = serialization.load_pem_public_key(f.read())
    except FileNotFoundError:
        print("This key does not exist >:(")
        exit(1)

    if option == "-m":
        message = content
    elif option == "-f":
        try:
            with open(content, "rb") as f:
                message = f.read()
        except FileNotFoundError:
            print("This key does not exist >:(")
            exit(1)
    else:
        print("Error reading content, please use -m or -f, for message or file respectively.\n")
        exit(1)
    encrypt(key,message,outfile)

