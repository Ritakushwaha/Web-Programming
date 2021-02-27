#C:\Users\rikushwa\OneDrive - Capgemini\Desktop>cd bs4

#C:\Users\rikushwa\OneDrive - Capgemini\Desktop\bs4>py sample_w4.py
#Enter - http://py4e-data.dr-chuck.net/comments_42.html
#Count 50
#Sum: 2553


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
sm = 0
cn = 0
for tag in tags:
	cn += 1
	sm += int(tag.contents[0])
    
print('Count', cn)
print('Sum:', sm)