import requests 

def HttpRequest(): 
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117'}
    cookies = {'PHPSESSID':'1plfje78cfg4142vhfrt3l4lon'}
    data = {'post':'hehe', 'post2':'hehe2'}
    url = "https://webhacking.kr/challenge/bonus-6/lv2.php"
    res = requests.post(url, headers=headers, cookies=cookies, data=data) 

    print(res.text)
    
if __name__ == '__main__': 
    HttpRequest()