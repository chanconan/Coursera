import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup

# Use BeautifulSoup
url = input('Enter - ')
# Read method will read the entire blob with new lines at the end as one big string
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
# And pulls out the value of href
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))