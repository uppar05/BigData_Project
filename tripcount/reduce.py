#!/usr/bin/python

import sys

last_key = None
last_count = 0
last_pacount = 0
last_tripd = 0.0
last_tip = 0.0
last_total = 0.0
#input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    line = line.strip()
    
    key, value = line.split('\t')
    pa_count, trip_d, tip, total = value.split(',')
    try:
	pa_count = int(pa_count)
	trip_d = float(trip_d)
	tip = float(tip)
	total = float(total)
    except ValueError:
	continue

    if last_key == key:
	last_count += 1
	last_pacount += pa_count
	last_tripd += trip_d
	last_tip += tip
	last_total += total
    else:
	if last_key:
	    print "%s\t%s,%s,%s,%s,%s" %(last_key, last_count, last_pacount, last_tripd, last_tip, last_total)
	last_key = key
	last_count = 0
	last_pacount = 0
	last_tripd = 0.0
	last_tip = 0.0
	last_total = 0.0

if last_key:
    print "%s\t%s,%s,%s,%s,%s" %(last_key, last_count, last_pacount, last_tripd, last_tip, last_total)
