#!/usr/bin/python

import sys
from sets import Set

#input comes from STDIN (stream data that goes to the program)

for line in sys.stdin:
    row = line.strip().split()

    if row[0] == "USAF":
        continue
    if len(row) == 33:
	weather_set = Set()
        time = row[2]
	key = time[:8]
	for i in range(12, 20):
	    #check if weather is specified
	    if row[i] != "**":
		weather_set.add(row[i])
	if len(weather_set) != 0:
	    value = ",".join(str(x) for x in weather_set)
	    print "%s\t%s" %(key, value)
	else:
	    print "%s\t**" %(key)
	
	
	
