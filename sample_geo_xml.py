import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

link = input ("Enter location: ")
print ("Retreiving", link)

data = urllib.request.urlopen(link).read().decode()
print ("Retreived", len(data), 'characters')	
	
cn = 0
sm = 0
data = ET.fromstring(data)
tags = data.findall('comments/comment')

for tag in tags:
	cn += 1
	sm = sm + int(tag.find('count').text)
	
print('Count:', cn)
print('Sum:', sm)