# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Input count: '))
# parse the position to an int and decrement the number by one to account for zero indexed lists.
position = int(input('Input position: ')) - 1

if len(url) < 1:
    print("No url was entered parsing default page...")
    url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'

i = 0  # set our loop index do 0
name = ''
while i < count:
    print(f"Retrieving: {url}")
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve all of the anchor tags
    tags = soup('a')
    # get all of the links using list comprehension.
    links = [tag.get('href', None) for tag in tags]
    name = tags[position].contents[0]
    url = links[position]
    i += 1  # increment our counter.

print(name)
