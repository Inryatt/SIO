from cryptography.hazmat.primitives.asymmetric import rsa
import sys,os
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import getpass
import binascii


def keygen():
    password = str.encode( getpass.getpass(prompt="gib pass:",stream=None))
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )  

    key = kdf.derive(password)
    print(f"your password now: {binascii.b2a_base64(key)}")
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )  
    kdf.verify(password,key)



if __name__== "__main__":
    keygen()