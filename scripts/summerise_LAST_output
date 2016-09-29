#!/usr/bin/env python

# Alignment_summerise_output_summeriser.py!

# Author: Luisa Teasdale

# This script summerises the output put produced by the script
# Alignment_summerise.py

# It prints out a tab delimited table with each taxon/header and the number of
# the alignments where the seuqence for this species represents 70% or more of
# the alignment length. The threshold can be changed.

# Usage:
# python Alignment_summerise_output_summeriser.py
# output_csv_file_from_Alignment_summerise.py.csv output_file.txt

from __future__ import print_function
from os import path
import csv
import sys

csv_file = sys.argv[1]
outfile = sys.argv[2]

prop_complete = {}

# open the csv file and calculate whether the sequence is greater than or equal
# to 70% of the alignment. If so count this towards the total for that header
# (if you had the same headers for the same taxa across files the count will be
# for each taxon).

with open(csv_file, 'r') as csv_file:
    table = csv.reader(csv_file, delimiter='\t')
    header = next(table)
    for row in table:
        header = row[1]
        # change 0.70 to any threshold you want to specify
        if float(row[4]) >= 0.70:
            prop_complete[header] = prop_complete.get(header, 0) + 1

# Print the final counts for each header in the specified output file

with open(outfile, 'w') as output_table:
    for key in prop_complete:
        print(key, prop_complete[key], sep='\t', file=output_table)
