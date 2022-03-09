from cryptography.hazmat.primitives.asymmetric import rsa
import sys,os
from cryptography.hazmat.primitives import serialization

def keygen(key_len):
    priv_key=rsa.generate_private_key(public_exponent=65537,key_size=key_len)
    pub_key=priv_key.public_key()
    print("""
              ██████  ██    ██ ██████  ██      ██  ██████     ██   ██ ███████ ██    ██ 
   __         ██   ██ ██    ██ ██   ██ ██      ██ ██          ██  ██  ██       ██  ██  
  /o \_____   ██████  ██    ██ ██████  ██      ██ ██          █████   █████     ████   
  \__/-="="`  ██      ██    ██ ██   ██ ██      ██ ██          ██  ██  ██         ██    
              ██       ██████  ██████  ███████ ██  ██████     ██   ██ ███████    ██    
                                                                         
                                                                         
        """)

   # print(f"PRIVKEY: {priv_key.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.PKCS8,encryption_algorithm=serialization.NoEncryption())}\nPUBKEY: {pub_key.public_bytes(encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo)}")
    with open("pub_key","w+") as f:
        f.write(pub_key.public_bytes(encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo).decode('ascii'))
    print(f"{pub_key.public_bytes(encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo).decode('ascii')} ")
    print("""            
                      _____      _            _         _  __          
  .--.               |  __ \    (_)          | |       | |/ /          
 /.-. '----------.   | |__) | __ ___   ____ _| |_ ___  | ' / ___ _   _ 
 \\'-' .--"--""-"-'   |  ___/ '__| \ \ / / _` | __/ _ \ |  < / _ \ | | |
  '--'               | |   | |  | |\ V / (_| | ||  __/ | . \  __/ |_| |
                     |_|   |_|  |_| \_/ \__,_|\__\___| |_|\_\___|\__, |
                                                                  __/ |
                                                                 |___/ 
        """)
    
    print(f"{priv_key.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.PKCS8,encryption_algorithm=serialization.NoEncryption()).decode('ascii')}")
    with open("priv_key","w+") as f:
        f.write(priv_key.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.PKCS8,encryption_algorithm=serialization.NoEncryption()).decode('ascii'))


if __name__== "__main__":
    key_len=sys.argv[1]
    keygen(int(key_len))
