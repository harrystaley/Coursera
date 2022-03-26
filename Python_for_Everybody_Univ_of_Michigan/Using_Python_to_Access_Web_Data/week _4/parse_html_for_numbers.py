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

url = input('URL: ')
if len(url) < 1:
    print("No url was entered parsing default page...")
    url = 'http://py4e-data.dr-chuck.net/comments_42.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
numbers = []
# Retrieve all of the span tags
tags = soup('span')
try:
    # get all of the numbers using list comprehension.
    numbers = [int(tag.contents[0]) for tag in tags]
except:
    print("Not all spans contain numbers.")

print(f"Count: {len(numbers)}")
print(f"Sum: {sum(numbers)}")
