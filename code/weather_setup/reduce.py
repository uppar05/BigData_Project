#!/usr/bin/python

import sys

last_date = None
last_weather = None
#input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    line = line.strip()
    
    date, weather = line.split('\t')
    

    if last_date == date:
        last_weather = weather and last_weather
    else:
	    if last_weather:
	        print "%s\t%s" %(last_date, last_weather)
	    last_date = date
	    last_weather = weather

if last_date:
    print "%s\t%s" %(last_date, last_weather)

