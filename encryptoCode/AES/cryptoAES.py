from Crypto.Cipher import AES
from Crypto.Hash import SHA256 as SHA

class myAES():
    def __init__(self, keytext, ivtext):
        hash = SHA.new()
        hash.update(keytext.encode('utf-8'))
        key = hash.digest()
        self.key = key[:16] # 16 bytes (192 bits (key[:24]) / 256 bits (key))

        hash.update(ivtext.encode('utf-8'))
        iv = hash.digest()
        self.iv = iv[:16] # 16 bytes

    def makeEnabled(self, plaintext):
        fillersize = 0 
        textsize = len(plaintext)
        if textsize % 16 != 0 :
            fillersize = 16 - textsize % 16 
        
        filler = '0' * fillersize
        header = '%d' %(fillersize)
        gap = 16 - len(header)
        header += '#' * gap

        return header+plaintext+filler  # TEXT Component (header + information + zeros )
    
    def encoding(self, plaintext):
        plaintext = self.makeEnabled(plaintext)
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        encodingMsg = aes.encrypt(plaintext.encode())
        return encodingMsg
    
    def decoding(self, Ciphertext):
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        decodingMsg = aes.decrypt(Ciphertext)

        header = decodingMsg[:16].decode() #    8############### (header) 
        fillersize = int(header.split('#')[0])#     8 (the number of zeros( empty space ))
        if fillersize != 0:
            decodingMsg = decodingMsg[16:-fillersize]
        else:
            decodingMsg = decodingMsg[16:]

        return decodingMsg

def main():
    keytext = 'helloWorld' # Crpyto key (24 bits of SHA hash value)
    ivtext = '1234' # initialization vector 64 bits (4 bytes)
    msg = 'python3x' # plaintext 

    myCipher = myAES(keytext, ivtext)
    ciphered = myCipher.encoding(msg)
    deciphered = myCipher.decoding(ciphered)

    print('ORIGINAL:\t%s' %msg)
    print('CIPHERED:\t%s' %ciphered)
    print('DECIPHERED:\t%s'%deciphered)


main()