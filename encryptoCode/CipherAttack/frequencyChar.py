def frequency_Analysise(msg):
    fa = {}
    for c in msg:
        if c in fa:
            fa[c] += 1
        else:
            fa[c] = 1
    
    s = sorted(fa.items(), key=lambda x:x[1], reverse=True) # dictionary sort (value standard)
    print(s)

if __name__ == '__main__':
    msg = '53%%#305))6*;4826)4%=\')4%);806*;48#8@60\'))85;1%(;;-%*8#83(88)5*#;46(;88*96*?;8)*%(;485);5*#2:*%(;4956*2(5*c4)8@8*;4069285);)6#8)4%%;1(%9;48081;8:8%1;48#85;4\')-485#528806*81(%9;48;(88;4(%?34;48)4%;161;;188;%?;'
    frequency_Analysise(msg)