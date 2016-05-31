#!/usr/bin/env python3

# duplicate_remover.py

from __future__ import print_function, division, absolute_import
from os import path

import docopt
import sys
import screed

__author__ = "Luisa Teasdale"

CLI_ARGS = """
USAGE:
duplicate_remover.py R1_FILE R2_FILE

This is an in progress script which will be able to remove reads from duplicate
fragments by taking both reads in a pair into account. At the moment this
script will go through two fastq files (left and right) and, assuming the fastq
files are in the same order, it will yield each pair of reads.

"""


def pairer(filename1, filename2):
    with screed.open(filename1) as reads1, \
         screed.open(filename2) as reads2:
            for i, (readl, readr) in enumerate(zip(reads1, reads2)):
                yield (i, readl, readr)


# If I am being run as a script...
if __name__ == '__main__':
    opts = docopt.docopt(CLI_ARGS)
    left_fastq =  opts['R1_FILE']
    right_fastq = opts['R2_FILE']
    for i, r1, r2 in pairer(left_fastq, right_fastq):
        print(i, r1.name, r2.name)
