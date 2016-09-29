#!/usr/bin/env python3

from __future__ import print_function
from os import path

import docopt
import sys
import screed
from collections import defaultdict

__author__ = "lteasnail"

CLI_ARGS = """
USAGE:
remove_short_seqs.py [options] <FASTAFILE>

OPTIONS:
-m MINIMUM   The minimum proportion of each sequence that must be real data

"""


def remove_seqs(fastafile, threshold):
    seqs = screed.open(fastafile)
    for seq in seqs:
        lenght = len(seq.sequence)
        count_real_data = 0
        sequen = seq.sequence
        for base in sequen:
            if base == "A" or base == "T" or base == "C" or base == "G":
                count_real_data += 1
        prop_real = count_real_data/float(lenght)
        if prop_real >= float(threshold):
            print(">", seq.name, "\n", sequen, file=sys.stdout)


# If I am being run as a script...

if __name__ == '__main__':
    opts = docopt.docopt(CLI_ARGS)
    fasta_file = opts['<FASTAFILE>']
    threshold = opts['-m']
    remove_seqs(fasta_file, threshold)
