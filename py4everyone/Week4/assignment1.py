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
tags = soup('span')
print(sum([int(tag.contents[0]) for tag in tags]))