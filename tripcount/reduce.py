#!/usr/bin/python

import sys

last_key = None
last_count = 0
#input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    line = line.strip()
    
    key, count = line.split('\t')
    
    try:
	count = int(count)
    except ValueError:
	#count is not a number, just ignore
	continue

    if last_key == key:
	last_count += count
    else:
	if last_key:
	    print "%s\t%s" %(last_key, last_count)
	last_key = key
	last_count = count

if last_key:
    print "%s\t%s" %(last_key, last_count)
