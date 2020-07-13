
def makeCodebook():
    decbook = {'5':'a','2':'b','#':'d','8':'e','1':'f','3':'g','4':'h','6':'i'
               ,'0':'l','9':'m','*':'n', '%':'o', '=':'p','(':'r',')':'s',';':'t'
               ,'?':'u','@':'v', ':':'y', '7':' '}

    encbook= {}
    for i in decbook: # key value : i 
        value = decbook[i]
        encbook[value] = i

    return encbook, decbook

def encrypt(msg, encbook):
    
    for i in msg:
        if i in encbook:
            msg = msg.replace(i, encbook[i])

    return msg

def decrypt(msg, decbook):

    for i in msg:
        if i in decbook:
            msg = msg.replace(i, decbook[i])

    return msg
    
if __name__ == '__main__':
    a = open('plain.txt','rt',encoding='utf-16')
    txt = a.read()
    a.close()

    encbook, decbook = makeCodebook()
    txt = encrypt(txt, encbook)
    
    a = open('encrypt.txt','wt+',encoding='utf-16') # wt+ : 파일을 생성하고 읽고 쓰는 기능
    a.write(txt)
    a.close()
