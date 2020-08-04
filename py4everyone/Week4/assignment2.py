import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Use BeautifulSoup
url = input('Enter URL: ')
count = int(input('Enter Count: '))
position = int(input('Enter Position: ')) - 1
# Read method will read the entire blob with new lines at the end as one big string
while count != 0:
    html = urllib.request.urlopen(url, context = ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    # And pulls out the value of href
    tags = soup('a')
    url = tags[position].get('href', None)
    if(count == 1):
        print(tags[position].contents)
    count -= 1
