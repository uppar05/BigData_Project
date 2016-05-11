#!/usr/bin/python

import sys

#input comes from STDIN (stream data that goes to the program)

for line in sys.stdin:
    row = line.strip().split()

    if row[0] == "USAF":
        continue
    if len(row) != 33:
        print row

print "done"

"""
    if len(row) == 33:
        time = row[2]
        print "%s\t1" %(key)
	
"""
	
