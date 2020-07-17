# Caesar Cipher Sentence 
# Receives the ciphertext as an argument and displays the result of moving 
# each character of the ciphertext by 1

def makeSentence(k):
    dec_msg = {}
    for i in range(26):
        tmp = (i+k)%26 + 65
        dec_msg[chr(tmp)] = chr(i+65)
    return dec_msg

def makeDecode(msg, key): # caesar
    ret = ''
    msg = msg.upper()
    sen = makeSentence(key)
    for c in msg:
        if c in sen:
            ret += sen[c]
        else:
            ret += c
    
    return ret

def attack(msg):
    for key in range(1,26):
        decodingMsg = makeDecode(msg, key)
        print("[%d]: %s" %(key,decodingMsg))

if __name__ == '__main__':
    msg = 'UGAMKZMBSMGQAVCUJMZBPZMMNQDMWVMBPZMM'
    attack(msg)