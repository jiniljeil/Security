import re

html_page = \
    """
    </head>
    <body><center>
    <div>
    <h3>PICTURE</h3><br>
    <img src="/static/images/2015-08-25_234806.jpg"/>
    <img src="/static/images/2015-08-25_234836.jpg"/>
    <img src="/static/images/2015-08-25_234910.jpg"/>"""

pattern = r'src=\S+"'
p = re.compile(pattern)
ret = p.findall(html_page)

if ret:
    for r in ret:
        print(r)
