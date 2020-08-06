import urllib.request, urllib.error, urllib.parse
import json
import ssl

api_key = False
if api_key is False:
    # This replaces the api_key to integer for conditional within while loop
    api_key = 42
    service_url = "http://py4e-data.dr-chuck.net/json?"
else:
    service_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
    
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

try:
    location = input('Enter location: ')
    params = dict()
    params['address'] = location
    if api_key is not False: params['key'] = api_key
    url = service_url + urllib.parse.urlencode(params)
    print('Retrieving URL', url)

    url_handle = urllib.request.urlopen(url, context=ctx)
    data = url_handle.read().decode()
    data = json.loads(data)

    print(data['results'][0]['place_id'])
except:
    print('Need a valid address')
