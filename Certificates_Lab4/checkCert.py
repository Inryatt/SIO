from cryptography import x509
import sys
import datetime
import os
import copy

def main(to_read,size=None):
    
    certs = {}

    if not size:
        with open(to_read,"rb") as f:
            pem_data = f.read()
        cert= x509.load_pem_x509_certificate(pem_data)
        certs[cert.subject] = cert
    else:
        count=0
        for c in os.listdir("/etc/ssl/certs"):
            if count<size:
                #print(f"TEST {c}")
                try:
                    with open("/etc/ssl/certs/"+c,"rb") as f:
                        pem_data = f.read()
                except IsADirectoryError:
                    continue
                cert= x509.load_pem_x509_certificate(pem_data)

                certs[cert.subject] = copy.deepcopy(cert)
                count+=1
            else:
                break
    
    for cert in certs:
        valid=validate(certs[cert])
        print(valid)

    #print(f"Not Valid Before: {cert.not_valid_before}")
    #print(f"Not Valid After: {cert.not_valid_after}")
    #print(f"SerialNum: {cert.serial_number}")

def validate(cert):
    now = datetime.datetime.now()

    if cert.not_valid_before > now or cert.not_valid_after < now:
        print("This certificate is not valid.")
        print(cert.subject)
        return False
    else:
        print("Valid certificate!")
        return True


if __name__=="__main__":
    
    to_read=sys.argv[1] 
    if len(sys.argv)>2:
        if sys.argv[2]== '*':
            size = 99999999999
        else:
            size = int(sys.argv[2])
    main(to_read,size)