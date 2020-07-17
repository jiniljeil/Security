# https://crackstation.net/buy-crackstation-wordlist-password-cracking-dictionary.htm
# $6$ (012) + salt 8 bytes (3 ~ 11) 
import ccrypt512 as crypt

def findPassword(passHash, dictfile):
    salt = passHash[3:11]
    with open(dictfile, 'r') as dfile:
        for word in dfile.readlines():
            word = word.strip('\n')
            cryptpw = crypt.sha512_crypt(word, salt)
            if cryptpw == passHash:
                return word
    
    return ''

if __name__ == '__main__':
    dictfile = 'dictionary.txt'
    with open('passwords.txt', 'r') as passFile:
        for line in passFile.readlines():
            data = line.split(':')
            user = data[0].strip()
            passwd = data[1].strip()
            word = findPassword(passwd, dictfile)
            if word:
                print('[id: %s] password: %s' %(user, word))
            else:
                print('Not Found')