#!/usr/bin/python

import sys
import operator

last_key = None
last_total = None
total_ride = {}
total_day = {}
#input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    line = line.strip()
    
    key, value = line.split('\t')
    
    date, neighbor = key.split(',')
    total_ride[neighbor] = total_ride.get(neighbor, 0) + int(value)
    total_day[neighbor] = total_day.get(neighbor, 0) + 1

sorted_ride = sorted(total_ride.items(), key = operator.itemgetter(1))
sorted_day = sorted(total_day.items(), key = operator.itemgetter(1))
print sorted_ride
print sorted_day
