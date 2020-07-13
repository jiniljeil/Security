
MSG = 'python3x'
t = MSG.encode('utf-8')
print(t) # b'python3x'

msg = b'python3x' # bytes object declaration 

for i in msg:
    print i,  # no new line 
