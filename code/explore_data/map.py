#!/usr/bin/env python

import sys
import csv
import StringIO

#input comes from STDIN (stream data that goes to the program)

for line in sys.stdin:
    csv_file = StringIO.StringIO(line)
    csv_reader = csv.reader(csv_file)
    for record in csv_reader:
        line = line.strip()
        data = line.split("\t")

        value = data[1].split(",")
        fare_amount = value[-6]

        try:
        fare_amount = float(fare_amount)
        except ValueError:
        continue

        if fare_amount > 48.01:
        fare_amount = 48.01
        if fare_amount < 0:
        fare_amount = 0

        print '%s' % (int((fare_amount-0.01)/4))


