import urllib.request, urllib.error, urllib.parse
import json


url = input('Enter url: ')
try:
    data = urllib.request.urlopen(url).read().decode()
    jsonData = json.loads(data)
    print('Sum is',sum([int(x['count']) for x in jsonData['comments']]))
except:
    print("Need a URL")