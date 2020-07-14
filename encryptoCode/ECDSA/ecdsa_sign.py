from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
from Crypto.Hash import SHA256 as SHA

def readPEM_ECC(pemfile):
    with open(pemfile, 'r') as h:
        key = ECC.import_key(h.read())
    
    return key

def ecdsa_sign(msg):
    privateKey = readPEM_ECC('privkey_ecdsa.pem')
    sha = SHA.new(msg)
    signer = DSS.new(privateKey,'fips-186-3')
    signature = signer.sign(sha)
    print("private Key:", privateKey)
    return signature

def ecdsa_verify(msg, signature):
    publicKey = readPEM_ECC('pubkey_ecdsa.pem')
    print("public Key:", publicKey)
    sha = SHA.new(msg)
    verifier = DSS.new(publicKey, 'fips-186-3')
    try:
        verifier.verify(sha, signature)
        print('Authentic')
    except ValueError:
        print('Not Authentic')
    
def main():
    msg = 'Security is very interesting'
    signature = ecdsa_sign(msg.encode('utf-8'))
    ecdsa_verify(msg.encode('utf-8'), signature)

main()

