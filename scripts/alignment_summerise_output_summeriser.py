#!/usr/bin/env python

# Alignment_summerise_output_summeriser.py!

from __future__ import print_function
from os import path
import csv
import sys

csv_file = sys.argv[1]
outfile = sys.argv[2]

prop_complete = {}

with open(csv_file, 'r') as csv_file:
    table = csv.reader(csv_file, delimiter='\t')
    header = next(table)
    for row in table:
        header = row[1]
        if float(row[4]) >= 0.70:
            prop_complete[header] = prop_complete.get(header, 0) + 1

with open(outfile, 'w') as output_table:
    for key in prop_complete:
        print(key, prop_complete[key], sep='\t', file=output_table)
