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
        print "%s\t1" %(key)
	
	
	
