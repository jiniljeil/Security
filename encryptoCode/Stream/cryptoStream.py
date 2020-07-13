from Crypto.Cipher import ARC4 
from Crypto.Hash import SHA256 as SHA

class myARC4():
    def __init__(self, keytext):
        self.key = keytext.encode()
    
    def encoding(self, plaintext):
        arc4 = ARC4.new(self.key)
        encodingMsg = arc4.encrypt(plaintext.encode())
        return encodingMsg
    
    def decoding(self, ciphertext):
        arc4 = ARC4.new(self.key)
        decodingMsg = arc4.decrypt(ciphertext)
        return decodingMsg

def main():
    keytext = 'helloWorld'
    msg = 'python3x'

    Cipher = myARC4(keytext)
    ciphered = Cipher.encoding(msg)
    deciphered = Cipher.decoding(ciphered)

    print('ORIGINAL:\t%s' %msg)
    print('CIPHERED:\t%s' %ciphered)
    print('DECIPHERED:\t%s' %deciphered)

main()