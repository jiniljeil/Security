from Crypto.Cipher import AES
from Crypto.Hash import SHA256 as SHA
from os import path
KSIZE = 1024

class myAES():
    def __init__(self, keytext, ivtext):
        hash = SHA.new()
        hash.update(keytext.encode('utf-8'))
        key = hash.digest()
        self.key = key[:16]

        hash.update(ivtext.encode('utf-8'))
        iv = hash.digest()
        self.iv = iv[:16]

    def makeEncodingInfo(self, fileName):
        fillersize = 0
        filesize = path.getsize(fileName)
        if filesize % 16 != 0:
            fillersize = 16 - filesize % 16
        filler = '0' * fillersize
        header = '%d' %(fillersize)
        gap = 16 - len(header)
        header += '#' * gap
        print(header)

        return header,filler
    
    def encoding(self, fileName):
        encfileName = fileName + '.enc'
        header,filler = self.makeEncodingInfo(fileName)
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)

        h = open(fileName, 'rb')
        hh = open(encfileName, 'wb+')
        enc = header.encode('utf-8')
        content = h.read(KSIZE)
        content = enc + content
        while content:
            if len(content) < KSIZE:
                content += filler.encode('utf-8')
            enc = aes.encrypt(content)
            hh.write(enc)
            content = h.read(KSIZE)
        h.close()
        hh.close()
    
    def decoding(self, encfileName):
        fileName = encfileName + '.dec'
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)

        h = open(fileName, 'wb+')
        hh = open(encfileName, 'rb')

        content = hh.read(8)
        dec = aes.decrypt(content)
        header = dec.decode()

        fillersize = int(header.split('#')[0])

        content = hh.read(KSIZE)
        while content:
            dec = aes.decrypt(content)
            if len(dec) < KSIZE:
                if fillersize != 0 :
                    dec = dec[:-fillersize]
            h.write(dec)
            content = hh.read(KSIZE)
        h.close()
        hh.close()

def main():
    keytext = 'samsjang'
    ivtext = '1234'
    fileName = 'plain.txt'
    encfileName = fileName + '.enc'

    Cipher = myAES(keytext, ivtext)
    Cipher.encoding(fileName)
    Cipher.decoding(encfileName)


if __name__=='__main__':
    main()
        
        