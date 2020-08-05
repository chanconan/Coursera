# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file and import

# If websites have SSL, need to import SSL
import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Use BeautifulSoup
url = input('Enter - ')
# Read method will read the entire blob with new lines at the end as one big string
html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
# And pulls out the value of href
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))