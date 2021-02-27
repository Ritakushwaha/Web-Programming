import urllib.request, urllib.parse, urllib.error
import json
import ssl

link = input ("Enter location: ")
print ("Retreiving", link)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data = urllib.request.urlopen(link).read().decode()
print ("Retreived", len(data), 'characters')	

try:
	js = json.loads(data)
except:
	js = None
	
cn = 0
sm = 0
for i in js['comments']:
	cn += 1
	sm = sm + int(i['count'])
	
print('Count:', cn)
print('Sum:', sm)