from  cryptography.hazmat.primitives.ciphers import Cipher,algorithms,modes
import os, sys
import secrets

     



def encrypt_file(infile,outfile,key,algo,iv,mode):

    if mode=='ECB':
        if algo == 'AES':
            cipher=Cipher(algorithms.AES(key),modes.ECB())
        elif algo=="ChaCha20":
            cipher=Cipher(algorithms.ChaCha20(key),modes.ECB())
        elif algo=="3DES":
            cipher=Cipher(algorithms.TripleDES(key),modes.ECB())
        else:
            print("Invalid Encryption")
            return
    elif mode=='CBC':
        if algo == 'AES':
            cipher=Cipher(algorithms.AES(key),modes.CBC(iv))
        elif algo=="ChaCha20":
            cipher=Cipher(algorithms.ChaCha20(key),modes.CBC(iv))
        elif algo=="3DES":
            cipher=Cipher(algorithms.TripleDES(key),modes.CBC(iv))
        else:
            print("Invalid Encryption")
            return
    else:
        print("Invalid mode")
        return
    encryptor=cipher.encryptor()

    fin=open(infile,'rb')
    fout=open(outfile,'wb')
    cgram=b''
    encryptor = cipher.encryptor()
    bread = 0
    while True:
        text = fin.read(16)
        bread +=len(text)

        if len(text) != 16:
            #PKCS
            missing_length = 16 - len(text)
            text += bytes([missing_length]*missing_length)
            cgram = encryptor.update(text) + encryptor.finalize()
            fout.write(cgram)
            break

        cgram = encryptor.update(text)
        if bread < 54:
            fout.write(text)
        else:
            fout.write(cgram)
    fin.close()
    fout.close()
    print("File encrypted")


def decrypt_file(infile,outfile,key,algo,iv,mode):
    print("Send 0.3BTC to the following wallet: mypEo145Fe8pSn5Rsodfh92CNikXgAwSna")
    if mode=='ECB':
        if algo == 'AES':
            cipher=Cipher(algorithms.AES(key),modes.ECB())
        elif algo=="ChaCha20":
            cipher=Cipher(algorithms.ChaCha20(key),modes.ECB())
        elif algo=="3DES":
            cipher=Cipher(algorithms.TripleDES(key),modes.ECB())
        else:
            print("Invalid Encryption")
            return
    elif mode=='CBC':
        if algo == 'AES':
            cipher=Cipher(algorithms.AES(key),modes.CBC(iv))
        elif algo=="ChaCha20":
            cipher=Cipher(algorithms.ChaCha20(key),modes.CBC(iv))
        elif algo=="3DES":
            cipher=Cipher(algorithms.TripleDES(key),modes.CBC(iv))
        else:
            print("Invalid Encryption")
            return
    else:
        print("Invalid mode")
        return

    fin=open(infile,'rb')
    fout=open(outfile,'wb')
    text=b''

    decryptor = cipher.decryptor()

    total_bytes = os.path.getsize(infile)
    read_bytes = 0
    while True:
        cgram = fin.read(16)
        read_bytes += len(cgram)
        if read_bytes == total_bytes:
            text = decryptor.update(cgram)
            padding = text[-1]
            text = text[0:16 - padding]
            fout.write(text)
            break
        text = decryptor.update(cgram)
        fout.write(text)
    
    fin.close()
    fout.close()
    print("File decrypted")
    
    

#if __name__=='__main__':
#    key=os.urandom(32)
#    iv=secrets.token_bytes(16)
#
#    text=sys.argv[1]
#    ciphertext=sys.argv[1]+".cgram"
#    output=sys.argv[1]+".text"
#    cipher=sys.argv[2]
#    mode = sys.argv[3]
#    encrypt_file(text,ciphertext,key,cipher,iv,mode)
#
#    decrypt_file(ciphertext,output,key,cipher,iv,mode)


if __name__=='__main__':
    key=os.urandom(32)
    iv=secrets.token_bytes(16)

    text=sys.argv[1]
    ciphertext=sys.argv[1]+".cgram"
    output=sys.argv[1]+".text"
    cipher=sys.argv[2]
    #mode = sys.argv[3]
    encrypt_file(text,ciphertext+".ecb.bmp",key,cipher,iv,'ECB')
    encrypt_file(text,ciphertext+".cbc.bmp",key,cipher,iv,'CBC')

    #decrypt_file(ciphertext,output,key,cipher,iv,mode)