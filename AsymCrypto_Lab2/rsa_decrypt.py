from cryptography.hazmat.primitives.asymmetric import rsa
import sys,os
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from  cryptography.hazmat.primitives.ciphers import Cipher,algorithms,modes

def decrypt(private_key,ciphertext):
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    
    with open("message.text","w+") as f:
        f.write(bytes.decode(plaintext))
        cipher=Cipher(algorithms.ChaCha20(key),modes.ECB())


if __name__== "__main__":
    if len(sys.argv)<4:
        print("ERROR.\nUsage:\n python3 rsa_encrypt.py <key> <file_to_decrypt>\nLook at them, they come from a place where they know they are not pure.")
        exit(1)
    key_file = sys.argv[1]
    content = sys.argv[2]

    try:
        with open(key_file, "rb") as f:
            key = serialization.load_pem_private_key(f.read(),password=None)
    except FileNotFoundError:
        print("This key does not exist >:(")
        exit(1)


    try:
        with open(content, "rb") as f:
            message = f.read()
    except FileNotFoundError:
        print("This message does not exist >:(")
        exit(1)
    decrypt(key,message)


