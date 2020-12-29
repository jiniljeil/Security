import pwn from *

#stage1 
argvs = [str(i) for i in range (100)]
argvs[ord('A')] = '\x00'
argvs[ord('B')] = '\x20\x0a\x0d'

#stage2 
with open('./stderr', 'a') as f:  
        f.write("\x00\x0a\x02\xff")

#stage3 
env_value = {'\xde\xad\xbe\xef':'\xca\xfe\xba\xbe'}

#stage4 
with open('./\x0a', 'a') as f:
        f.write('\x00\x00\x00\x00')

#stage5 
argvs[ord('C')] = '11111' # port number

target = process(executable='/home/input2/input', argv=argvs, stderr=open('./stderr'), env = env_value)

target.sendLine('\x00\x0a\x00\xff')

conn = remote('localhost','11111')
conn.send('\xde\xad\xbe\xef')
target.interactive()
