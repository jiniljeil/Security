from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256 as SHA

# Prime factorization crypto

def readPEM(pemfile):
    h = open(pemfile, 'r')
    key = RSA.importKey(h.read())
    h.close()
    return key

def rsa_encoding(msg):
    public_key = readPEM('publickey.pem')
    cipher = PKCS1_OAEP.new(public_key)
    encData = cipher.encrypt(msg)
    return encData

def rsa_decoding(msg):
    private_key = readPEM('privatekey.pem')
    cipher = PKCS1_OAEP.new(private_key)
    decData = cipher.decrypt(msg)
    return decData

def main():
    msg = 'Security is very interesting'
    ciphered = rsa_encoding(msg.encode('utf-8'))
    print(ciphered)
    deciphered = rsa_decoding(ciphered)
    print(deciphered)

main()
