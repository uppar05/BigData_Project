#!/usr/bin/python

import sys
from sets import Set

def classifyW(w):
    if w >= 0 and w <= 19:
	return "Cloud"
    elif w >= 30 and w <= 39:
	return "Dust"
    elif (w >= 40 and w <= 49) or w == 28:
	return "Fog"
    elif (w >= 50 and w <= 69) or w == 20 or w == 21 or w == 24:
	return "Rain"
    elif (w >= 70 and w <= 79) or w == 22 or w == 23:
	return "Snow"
    elif (w >= 80 and w <= 99) or w == 25 or w == 26 or w == 27 or w == 29:
	return "Shower"

weather_list = Set()
lastKey = None
#input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:  
    key, value = line.strip().split('\t')

    if key == lastKey:
	value = value.split(',')
	for i in range(len(value)):
	    #print value[i]
	    weather_list.add(value[i])
	#print weather_list
    #when key != lastKey
    else:
	if len(weather_list) > 2 and ("**" in weather_list):
	    weather_list.remove("**")
	    #print weather_list
	    unique_list = Set()
	    for w in weather_list:
		try:
		    w = int(str(w))
		except ValueError:
		    continue
		s = classifyW(w)
		unique_list.add(s)
	    ws = "/".join(str(x) for x in unique_list)
	    print "%s\t%s" %(lastKey, ws)
	#only ** exists in the set
	elif lastKey != None:
	    print "%s\tCloud" %(lastKey)
	lastKey = key
	weather_list = Set()
	weather_list.add(str(x) for x in value.split(','))

#deal with last lines
if len(weather_list) > 2 and ("**" in weather_list):
    weather_list.remove("**")
    #print weather_list
    unique_list = Set()
    for w in weather_list:
	try:
	    w = int(str(w))
	except ValueError:
	    #count is not a number, just ignore
	    continue
	s = classifyW(w)
	unique_list.add(s)
    ws = "/".join(str(x) for x in unique_list)
    print "%s\t%s" %(key, ws)
#only ** exists in the set
else:
    print "%s\tCloud" %(key)
