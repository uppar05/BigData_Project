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
    
    date, neighbor, weather = key.split(',')
    if weather not in total_ride:
        total_ride[weather] = {}
        total_day[weather] = {}
    total_ride[weather][neighbor] = total_ride[weather].get(neighbor, 0) + int(value)
    total_day[weather][neighbor] = total_day[weather].get(neighbor, 0) + 1

for k in total_ride.keys():
    print k
    sorted_ride = sorted(total_ride[k].items(), key = operator.itemgetter(1))
    print sorted_ride

print '-----------------------------------------------------------------'

for k in total_day.keys():
    print k
    sorted_day = sorted(total_day[k].items(), key = operator.itemgetter(1))
    print sorted_day

