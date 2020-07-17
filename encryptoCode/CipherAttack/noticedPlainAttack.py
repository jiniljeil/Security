def makePattern(word):
    tmp = {} 
    res = [] 
    index = 0 
    for c in word:
        if c in tmp:
            res.append(tmp[c])
        else:
            tmp[c] = str(index)
            res.append(str(index))
            index += 1
    return ';'.join(res)

def findPattern(msg, word):
    pattern = makePattern(word)
    wordLength = len(word)
    pos = 0
    while True:
        data = msg[pos: pos + wordLength]
        if len(msg) < (pos + wordLength):
            break
        
        ptrn = makePattern(data)
        if pattern == ptrn:
            return data

        pos += 1

if __name__ == '__main__':
    msg = '53%%#305))6*;4826)4%=\')4%);806*;48#8@60\'))85;1%(;;-%*8#83(88)5*#;46(;88*96*?;8)*%(;485);5*#2:*%(;4956*2(5*c4)8@8*;4069285);)6#8)4%%;1(%9;48081;8:8%1;48#85;4\')-485#528806*81(%9;48;(88;4(%?34;48)4%;161;;188;%?;'
    known_plain = ['goodglass', 'mainbranch']
    for p in known_plain:
        t = findPattern(msg, p)
        print('[%s]=%s' %(p, t))
