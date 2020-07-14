from Crypto.Signature import pkcs1_15
from Crypto.PublicKey import RSA 
from Crypto.Hash import SHA256 as SHA
# public key signature is signatured by private key of user
# it verifies the encoded information on public key 

def readPEM(pemfile):
    h = open(pemfile, 'r')
    key = RSA.importKey(h.read())
    h.close()
    return key

def rsa_sign(msg):
    private_key = readPEM('privatekey.pem')
    public_key = private_key.publickey()
    h = SHA.new(msg)
    signature = pkcs1_15.new(private_key).sign(h) # signature by private key of user
    print("Private Key :", private_key)
    print("Public Key :", public_key)
    return public_key, signature

def rsa_verify(msg, public_key, signature):
    h = SHA.new(msg)
    try:
        pkcs1_15.new(public_key).verify(h,signature)
        print('Authentic')
    except Exception as e:
        print(e)
        print('Not Authentic')
    
def main():
    msg = 'Security is very interesting'
    public_key, signature = rsa_sign(msg.encode('utf-8'))
    rsa_verify(msg.encode('utf-8'), public_key, signature)

main()