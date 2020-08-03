from urllib.request import urlopen, Request

user_agent = 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'
cookie = '~~~' # After receiving the cookie, Change the content you want 

def cookieSpoof(url):
    req = Request(url)
    req.add_header('User-Agent', user_agent)
    req.add_header('Cookie', cookie)
    with urlopen(req) as h:
        print(h.read())
    
def main():
    url = 'http://www.google.com'
    cookieSpoof(url)
    
main()
