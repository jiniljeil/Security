import base64
import hashlib

string = 'admin'
md5 =''

for c in string:
    result = hashlib.md5(c.encode()).hexdigest()
    md5 += result
    print(c, result)

b = md5.encode("UTF-8") 
encode_result = base64.b64encode(b)
print(encode_result)