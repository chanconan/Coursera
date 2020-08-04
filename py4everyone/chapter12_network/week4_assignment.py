import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# Does not return headers
fileHandle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# Every line is in bytes or encoded, so it needs to be decoded to return a string
for line in fileHandle:
    print(line.decode().strip())