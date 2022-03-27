import json
import ssl
import urllib.error
import urllib.request

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_42.json'

print('Retrieving json data: ', url)
uh = urllib.request.urlopen(url, context=ctx)
json_data = uh.read()
json_obj = json.loads(json_data)

# collect the counts using list comprehension.
counts = [int(item['count']) for item in json_obj['comments']]
# convert the next nodes to ints using list comprehension.
print(f"count: {len(counts)}")
print(f"sum: {sum(counts)}")
