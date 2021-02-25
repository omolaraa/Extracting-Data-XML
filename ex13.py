import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

countlist = list()
address = input('Enter location: ')
print('Retrieving', address)
uh = urllib.request.urlopen(address, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)
counts = tree.findall('comments/comment')
print('User count:', len(counts))
for count in counts:
    nums = count.find('count').text
    nums = int(nums)
    countlist.append(nums)
print(sum(countlist))
