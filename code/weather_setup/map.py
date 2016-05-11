#!/usr/bin/python

import sys

#input comes from STDIN (stream data that goes to the program)

for line in sys.stdin:
    row = line.strip().split()

    if row[0] == "USAF":
        continue

    time = row[2]
    weather = row[12:20]
    clean_weather = True
    for w in weather:
        if w != '**':
            clean_weather = False
            break
    date = time[4:8]
    print date, "\t", clean_weather


