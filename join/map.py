#!/usr/bin/python

import sys

#input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    key, value = line.strip().split("\t")
    #indicate we are reading trips
    if key == "date":
	continue
    print "%s\t%s" %(key, value)
