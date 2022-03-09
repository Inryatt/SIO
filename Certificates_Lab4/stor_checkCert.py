from cryptography import x509
import sys
import datetime
import os
import copy

def main(serv_cert,intermediate_cert):
    
    root_ca_store = {}
    store={}
    intermediate_ca_store={}

    #Loadserver cert
    load_certificate(serv_cert,store)

    #load intermediate ca 
    load_certificate(intermediate_cert,intermediate_ca_store)



    for c in os.listdir("/etc/ssl/certs"):
        try:
            load_certificate("/etc/ssl/certs/"+c, root_ca_store)
        except IsADirectoryError:
            continue

    
    print(f"Root CA Certs: {len(root_ca_store)}")
    print(f"Intermediate CA Certs: {len(intermediate_ca_store)}")

    print(f"Server Certs: {len(store)}")

    chain =[]
    cert=store[list(store)[0]]
    print(build_chain(cert,intermediate_ca_store,root_ca_store,chain))

    #print(f"Not Valid Before: {cert.not_valid_before}")
    #print(f"Not Valid After: {cert.not_valid_after}")
    #print(f"SerialNum: {cert.serial_number}")

def validate(cert,issuer,target_purpose):
    now = datetime.datetime.now()

    if cert.not_valid_before > now or cert.not_valid_after < now:
        print("This certificate is not valid.")
        print(cert.subject)
        return False

    # Date: Done
    # Purpose -- in documentation

         # bottom level is tls access
         # all others others should be allowed to create CAs
    # Cert signature
    #       tbs_signature_bytes , signature
    #   download and check crl or ocsp -- in documentation




    print("Valid certificate!")
    return True

def load_key():
    pass


def load_certificate(cert, dest):
    with open(cert,"rb") as f:
            pem_data = f.read()
    cert= x509.load_pem_x509_certificate(pem_data)
    dest[cert.subject] = copy.deepcopy(cert)



def build_chain(cert,intermediate_ca,root_ca,chain):
    chain.append(cert)
    if cert.issuer in intermediate_ca:
        issuer = intermediate_ca[cert.issuer]
        return build_chain(issuer,intermediate_ca,root_ca,chain)
    if cert.issuer in root_ca:
        issuer=root_ca[cert.issuer]
        chain.append(issuer)
        print(chain)
        return True

    return False

if __name__=="__main__":
    serv_cert=sys.argv[1]
    intermediate_cert=sys.argv[2]
    main(serv_cert,intermediate_cert)