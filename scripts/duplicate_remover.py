#!/usr/bin/env python3

from __future__ import print_function, division, absolute_import
from os import path

import docopt
import sys
import screed

__author__ = "lteasnail"

CLI_ARGS = """
USAGE:
thing.py [options]

OPTIONS:
 -l LEFT       left hand reads fastq file
 -r RIGHT      Right hand reads fastq file

"""


def pairer(filename1, filename2):
    with screed.open(filename1) as reads:
        with screed.open(filename2) as reads:
            counts = 0
            for read in seqfile:
                counts += 1
                reads = (counts, read, )
                yield reads


# If I am being run as a script...
if __name__ == '__main__':
    opts = docopt.docopt(CLI_ARGS)
    left_fastq = opts['-l']
    right_fastq = opts['-r']
    counts = pairer(left_fastq, right_fastq)
    print(*counts, file=sys.stderr)
