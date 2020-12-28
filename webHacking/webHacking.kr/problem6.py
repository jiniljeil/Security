import base64

arr_ch = ['!','@','$','^','&','*','(',')']
val_id = "admin"
val_pw = "nimda"

tmp_id = val_id.encode("UTF-8")
tmp_pw = val_pw.encode("UTF-8")

result_id = base64.b64encode(tmp_id)
result_pw = base64.b64encode(tmp_pw)

for i in range(19):
    result_id = base64.b64encode(result_id)
    result_pw = base64.b64encode(result_pw)

for k in result_id: 
    if( ord(k) >= 49 and ord(k) <= 56): # 1 ~ 8
        result_id = result_id.replace(k,arr_ch[ord(k)-49])

for k in result_pw:
    if( ord(k) >= 49 and ord(k) <= 56): # 1 ~ 8
        result_pw = result_pw.replace(k,arr_ch[ord(k)-49])
        
print(result_id)
print(result_pw)

