# encrypto on 3DES CBC mode 
# decrypto the ciphertext on plaintext
# pip install pycryptodome==3.4.3
# 3DES have the block size of 64 bits

from Crypto.Cipher import DES3 
from Crypto.Hash import SHA256 as SHA 

class myDES():
    def __init__(self, keytext, ivtext): # class constructor/ keytext: string, ivtext: string to initiallization vector  
        hash = SHA.new()
        hash.update(keytext.encode('utf-8'))
        key = hash.digest()
        self.key = key[:24]

        hash.update(ivtext.encode('utf-8'))
        iv = hash.digest()
        self.iv = iv[:8]

    def encode(self, plaintext):
        plaintext = makeEightString(plaintext)
        des3 = DES3.new(self.key, DES3.MODE_CBC, self.iv) # CBC mode Encoding 
        encodeMsg = des3.encrypt(plaintext.encode())
        return encodeMsg
    
    def decode(self, ciphertext):
        des3 = DES3.new(self.key, DES3.MODE_CBC, self.iv)
        decodeMsg = des3.decrypt(ciphertext)
        return decodeMsg

def makeEightString(msg): # it executed when the plaintext is longer than 8 bytes.
    msglen = len(msg)
    filler = ''
    if msglen % 8 != 0:
        filler = '0' * (8 - msglen % 8) # 0 : (0 to maintain 8 of the drainage system)
    msg += filler
    return msg

def main():
    keytext = 'helloWorld' # Crypto key (24 bits of SHA hash value)
    ivtext = '1234' # initialization vector 64 bits (4 bytes)
    msg = 'python3xab' # plaintext 

    myCipher = myDES(keytext, ivtext)
    ciphered = myCipher.encode(msg)
    deciphered = myCipher.decode(ciphered)

    print('ORIGINAL:\t%s' %msg)
    print('CIPHERED:\t%s' %ciphered)
    print('DECIPHERED:\t%s'%deciphered)


main()