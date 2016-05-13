#!/usr/bin/python

import sys

last_key = None
last_total = None
#input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    line = line.strip()
    
    key, value = line.split('\t')
    
    if last_key == key:
        last_total += 1 
    else:
        if last_key:
            print "%s\t%s" % (last_key, last_total)
        last_key = key
        last_total = 1

if last_key:
    print "%s\t%s" % (last_key, last_total)
