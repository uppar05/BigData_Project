#!/usr/bin/python

import sys

#input comes from STDIN (stream data that goes to the program)

for line in sys.stdin:
    row = line.strip().split(",")

    if row[0] == "VendorID":
        continue
    if len(row) == 19:
        time = row[1]
        date, hour = time.split(" ")
        year, month, day = date.split("-")
        key = "%s%s%s" %(year, month, day)
	#to reduce those invalid trip records
	if int(row[3]) >= 0 and float(row[4]) >= 0 and float(row[-4]) >= 0 and float(row[-1]) >= 0:
	    value = "%s,%s,%s,%s" %(row[3], row[4], row[-4], row[-1])
            print "%s\t%s" %(key, value)
	
	
	
