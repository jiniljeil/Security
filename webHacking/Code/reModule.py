import re

pattern = r'\w+'
p = re.compile(pattern)
text = '     1Ag2d35      '
ret1 = p.match(text) # check on the starting section of string 
ret2 = p.search(text) # check whether the pattern exists or not in the string 

if ret1:
    print('match result: [%s]' %ret1.group())
if ret2:
    print('search result [%s]' %ret2.group())