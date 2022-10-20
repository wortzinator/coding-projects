import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
webinfo = urllib.request.urlopen(url)
web = webinfo.read().decode()


info = json.loads(web)
print('User count: ', len(info))

for items in info:
    print('Name', items['name'])
    print('Count', items['count'])