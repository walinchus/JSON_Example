import urllib, json
import scraperwiki
url = "https://data.police.uk/api/forces"
response = urllib.urlopen(url)
data = json.loads(response.read())
print data 
print len(data)
record = {}
for i in data: 
  print i['name']
  if i['id'] == 'wiltshire':
    print "This is Wiltshire"
    #To look for text in a string: 
    if 'wilt' in i['id']:
      print "It contains 'wilt'"
  record['idcode'] = i['id']
  record['fullname'] = i['name']
  scraperwiki.sqlite.save(['idcode'], record)

