import ssl
import urllib.error
import urllib.request
from xml.etree import ElementTree

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

print('Retrieving xml data: ', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ElementTree.fromstring(data)
count_nodes = tree.findall('.//count')
# convert the next nodes to ints using list comprehension.
counts = [int(node.text) for node in count_nodes]
print(f"count: {len(counts)}")
print(f"sum: {sum(counts)}")
