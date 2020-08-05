import urllib.error, urllib.parse, urllib.request
import xml.etree.ElementTree as ET
import ssl

def xmlParser(address):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    print("Retreiving URL " + address)
    urlHandler = urllib.request.urlopen(address, context = ctx).read()
    print("Retrieved", len(urlHandler), 'characters')
    locTree = ET.fromstring(urlHandler)
    counts = locTree.findall('.//count')
    print('Count:',len(counts))
    print('Sum:',sum([int(count.text) for count in counts]))
    # counts = locTree.findall('.//count')
    # for count in counts:
    #     print(count.text)

address = input('Enter address: ')
xmlParser(address)