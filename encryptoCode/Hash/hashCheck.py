from hashlib import sha256 as SHA
SIZE = 1024 * 256 

def getFileHash(filename):
    sha = SHA()
    h = open(filename, 'rb')
    content = h.read(SIZE)

    while content:
        sha.update(content)
        content = h.read(SIZE)
    h.close()

    hashValue = sha.digest()
    return hashValue

def hashCheck(file1, file2):
    hashValue1 = getFileHash(file1)
    hashValue2 = getFileHash(file2)
    
    if hashValue1 == hashValue2:
        print("Two Files are Same")
    else:
        print("Two Files are different")
    
def main():
    file1 = 'plain1.txt'
    file2 = 'plain2.txt'
    hashCheck(file1, file2)

main()