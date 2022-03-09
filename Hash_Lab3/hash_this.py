from cryptography.hazmat.primitives.asymmetric import rsa
import sys,os
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from random import random


def hash_this(data):
    digest = hashes.Hash(hashes.SHA256())
    digest.update(data)
    data =digest.finalize()

    with open("output.txt","wb") as f:
        f.write(data)



if __name__=="__main__":
    pass 
    input = sys.argv[1]
    with open(input,"rb") as f:
        data =f.read()
    hash_this(data)