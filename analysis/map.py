#!/usr/bin/python

import sys

#input comes from STDIN (stream data that goes to the program)

for line in sys.stdin:
    row = line.strip().split(",")

    if len(row) == 7:
	#weather is key     
	key = row[-1]
	value = "%s,%s,%s,%s,%s" %(row[1], row[2], row[3], row[4], row[5])
	print "%s\t%s" %(key, value)
	
	
	
