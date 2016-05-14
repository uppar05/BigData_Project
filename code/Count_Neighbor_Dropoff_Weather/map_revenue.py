#!/usr/bin/python

import sys

#input comes from STDIN (stream data that goes to the program)

for line in sys.stdin:
    row = line.strip().split(",")

    if len(row) < 10 or row[0] == "VendorID":
        continue

    time = row[1]
    date, hour = time.split(" ")
    year, month, day = date.split("-")
    drop_off = row[-1]
    weather = row[-3].split('/')
    for w in weather:
        key = "%s%s%s,%s,%s" % (year, month, day, drop_off, w)
        print "%s\t1" % (key)

    
	#to reduce those invalid trip records
#    print "%s\t1" % (key)

"""
	if int(row[3]) >= 0 and float(row[4]) >= 0 and float(row[-4]) >= 0 and float(row[-1]) >= 0:
	    value = "%s,%s,%s,%s" %(row[3], row[4], row[-4], row[-1])
            print "%s\t%s" %(key, value)
	
"""
