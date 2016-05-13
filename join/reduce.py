#!/usr/bin/python

import sys

taxi_list = []
weather_list = []
lastKey = None
#input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    line = line.strip()
    
    key, value = line.split('\t')
    value_list = value.split(',')
    
    if key == lastKey:
	if len(value_list) == 1:
            weather_list.append((key, value))
	elif len(value_list) == 5:
            taxi_list.append((key, value))	
    #when key != lastKey
    else:
	if len(taxi_list) != 0 and len(weather_list) != 0:
	    for (tKey, tValue) in taxi_list:
    		for (wKey, wValue) in weather_list:
        	    if tKey == wKey:
            		print "%s,%s,%s" %(tKey, tValue, wValue)
	taxi_list = []
	weather_list = []
	if len(value_list) == 1:
            weather_list.append((key, value))
	elif len(value_list) == 5:
            taxi_list.append((key, value))
	lastKey = key

#deal with last lines
if len(taxi_list) != 0 and len(weather_list) != 0:
    for (tKey, tValue) in taxi_list:
	for (wKey, wValue) in weather_list:
       	    if tKey == wKey:
        	print "%s,%s,%s" %(tKey, tValue, wValue)	    

