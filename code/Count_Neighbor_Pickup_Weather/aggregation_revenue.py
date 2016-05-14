#!/usr/bin/python

import sys
import operator

last_key = None
last_total = None
total_revenue = {}
total_day = {}
#input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    line = line.strip()

    try:
        key, value = line.split('\t')        
    except:
        continue
    
    date, neighbor, weather = key.split(',')
    if weather not in total_revenue:
        total_revenue[weather] = {}
        total_day[weather] = {}
    total_revenue[weather][neighbor] = total_revenue[weather].get(neighbor, 0) + float(value)
    total_day[weather][neighbor] = total_day[weather].get(neighbor, 0) + 1

for k in total_revenue.keys():
    print k
    sorted_revenue = sorted(total_revenue[k].items(), key = operator.itemgetter(1))
    print sorted_revenue

print '-----------------------------------------------------------------'

for k in total_day.keys():
    print k
    sorted_day = sorted(total_day[k].items(), key = operator.itemgetter(1))
    print sorted_day

