#!/usr/bin/env python

# Alignment_summerise.py!

from __future__ import print_function
from os import path
# The fasta parser.
import screed
# Does what a dictionary does, essentially the same as
# dicti[word] = dicti.get(word,0) + 1
from collections import Counter, OrderedDict
import docopt
import sys

__author__ = "lteasnail"

CLI_ARGS = """
USAGE:
alignment_summerise.py [options] <FASTAFILES> ...

OPTIONS:
 -t TYPE        If PROT the program assumes you have an amino acid alignment if
                NUC the program assumes the alignments are in nulceotides.


Alignment summeriser

This program goes through the specified fasta MSA's and provides some summary
statistics.

You need to have python-screed and python-docopt installed.

e.g. python ambig_counter.py -t PROT *.fasta > Summary_stats.txt

"""

# This function counts the number of ambiguous bases per sequence per file,
# then works out the proportion of ambiguous sites and put them all in a
# dictionary


def count_data(filename, data_char):
    ambigs = OrderedDict()
    for seq in screed.open(filename):
        seq_name = seq.name
        seq = seq.sequence
        length = len(seq)

        counter = Counter()
        for base in seq:
            counter[base] += 1

        num_data = 0
        for base_type in data_char:
            num_data += counter.get(base_type, 0)
        if length == 0:
            prop_data = 0
        else:
            prop_data = (num_data) / float(length)

        ambigs[seq_name] = (length, prop_data, num_data)
    return ambigs


# This function runs the count_ambig function for each file and outputs the
# stats to a tab demlim file


def print_prop_data(files, data_char, table_file=sys.stdout):
    print('Filename\tSeq_header\tLength_of_seq\tData_sites\tProportion_data',
          file=table_file)
    for filename in files:
        all_prop_ambig = count_data(filename, data_char)
        for seq_name, (length, prop_data, num_data) in all_prop_ambig.items():
            print(filename, seq_name, length, num_data, prop_data, sep='\t',
                  file=table_file)


# If I am being run as a script...
if __name__ == '__main__':
    opts = docopt.docopt(CLI_ARGS)
    typee = opts['-t']
    files = opts['<FASTAFILES>']
    if typee == "PROT":
        data_char = "ABCDEFGHIKLMNPQRSTVWYZ*"
    else:
        data_char = "ACGTacgt"
    print('counting...', file=sys.stderr)
    print_prop_data(files, data_char)
    print('Finished counting data sites', file=sys.stderr)
