#!/usr/bin/env python

import sys

Last_key = None
total = 0

#input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    line = line.strip()
    
    key, value = line.split('\t')    

    if key == Last_key:
        total += 1
    else:
        if Last_key:
            print "%s\t%s" % (Last_key, total)
        Last_key = key
        total = 1

if Last_key:
    print "%s\t%s" % (Last_key, total)

    
