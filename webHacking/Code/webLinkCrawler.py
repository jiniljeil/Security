from urllib.request import urlopen, Request
import re
import sys

user_agent = 'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0;  rv:11.0) like Gecko' # User-Agent for IE 11
href_links = []
		
def getLinks(doc, home, parent):
    global href_links
    href_pattern = [r'href=\S+"', r'href=\S+ ', r'href=\S+\'']
    tmp_urls = []
    
    # Save HTML URL in the given URL
    for n in range(len(href_pattern)):
        tmp_urls += re.findall(href_pattern[n], doc, re.I)
            
    for url in tmp_urls:
        url = url.strip()		
        url = url.replace('\'', '"')
        
        if url[-1] is ' ' or url.find('"') is -1: # quotation mark missed
            url = url.split('=')[1]
        else:
            url = url.split('"')[1]
        
        if len(url) is 0:
            continue
                
        if url.find('http://') is -1:
            if url[0] == '/':
                url = home + url
            elif url[:2] == './':
                url = 'http://' + parent + url[1:]	
            else:
                url = 'http://' + parent + '/' + url
                                
        if url in href_links:
            continue
        
        if '.html' not in url:            
            href_links.append(url)
            continue
        
        runCrawler(home, url)	
	
def readHtml(url):				
    try:
        req = Request(url)
        req.add_header('User-Agent', user_agent)
        h = urlopen(req) 
        doc = h.read()
        h.close()
    except Exception as e:
        print('ERROR: %s' %url)
        print(e)
        return None		
    
    return doc.decode()
	
	
def runCrawler(home, url):
    global href_links
    href_links.append(url)
    
    print ('GETTING ALL LINKS in [%s]' %url)		
    try:
        doc = readHtml(url)
        if doc is None:
            return        
            
        tmp = url.split('/')
        #if '.' in tmp[-1]:
        #    tmp = tmp[:-1]
            
        parent = '/'.join(tmp[2:])        
        getLinks(doc, home, parent)
    except KeyboardInterrupt:
        print('Terminated by USER..Saving Crawled Links')
        finalize()
        sys.exit(0)
            
    return	
	
def finalize():
    with open('crawled_links.txt', 'w+') as f:
        for href_link in href_links:
            f.write(href_link+'\n')	
    print('+++ CRAWLED TOTAL LINKS: [%s]' %len(href_links))
	
def main():
    targeturl = 'http://www.google.com' # URL 
    home = 'http://' + targeturl.split('/')[2]
    
    print('+++ WEB LINK CRAWLER START > [%s]' %targeturl)
    runCrawler(home, targeturl)
    finalize()
		

main()
