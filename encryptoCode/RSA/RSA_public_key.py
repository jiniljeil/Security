from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

def rsa_encoding(msg):
    private_key = RSA.generate(1024)
    public_key = private_key.publickey()
    cipher = PKCS1_OAEP.new(public_key)
    encData = cipher.encrypt(msg)
    print (encData) # encoded text

    cipher = PKCS1_OAEP.new(private_key)
    decData = cipher.decrypt(encData)
    print(decData) # decoded text

def main():
    msg = 'Security is very interesting'
    rsa_encoding(msg)

main()