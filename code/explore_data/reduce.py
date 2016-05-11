#!/usr/bin/env python

import sys

Last_key = None
Last_count_sum = None

fare_range = ["0,4", "4.01,8", "8.01,12", "12.01,16", "16.01,20", "20.01,24", "24.01,28", "28.01,32", "32.01,36", "36.01,40", "40.01,44", "44.01,48", "48.01,infinite"]
fare_count = [0]*13

#input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    key = line.strip()

    try:
        key = int(key)
    except ValueError:
        continue

    fare_count[key] += 1    

for i in range(0, 13):
    if fare_count[i] > 0:
        print "%s\t%s" % (fare_range[i], fare_count[i])

