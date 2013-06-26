import json
import urllib2

gh = urllib2.urlopen('http://data.sfgov.org/resource/w969-5mn4.json').read()

data = json.dumps(dh)
list2= []

for entry in data:
	latitude = str(entry['latitude']
	longitude = str(entry['longitude'])
	t = (latitude, longitude)
	list2.append(t)

#get location, find 20 closest racks within a X mile, radius




