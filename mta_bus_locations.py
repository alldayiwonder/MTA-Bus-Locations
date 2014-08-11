#!/usr/bin/env python

import sys
import urllib2
import json
import pprint

key = sys.argv[1]
bus = sys.argv[2] 

#call the url with api key and bus line
url = "http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key={}&VehicleMonitoringDetailLevel=calls&LineRef={}".format(key,bus)

#load jSon into a Python object
r = urllib2.urlopen(url)
result = json.load(r)
data = result['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
#pprint.pprint(data)

#print the subject bus line
print "Bus Line: ", bus 

#print the number of active buses
count=0 
for i in data:
	count +=1
print "Number of Active Buses: ", count

print "Locations: (lat/long) " 

#print the current locations of each bus in the route
for i in data:
	latitude = i['MonitoredVehicleJourney']['VehicleLocation']['Latitude'] 
	longitude = i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
	print latitude, longitude 






