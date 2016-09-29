#!/usr/bin/env python3

from __future__ import print_function

from os import path
# The fasta parser.
import screed
# For taking arguments from the command line.
import sys
from collections import Counter, OrderedDict
import docopt


__author__ = "lteasnail"

CLI_ARGS = """
USAGE:
ambig_counter.py [-t THRESHOLD] <FASTAFILES>...

OPTIONS:
-t THRESHOLD   If the proportion of ambiguous sites for a sequence is above
               this threshold the sequence will be replaced with a dummy
               sequence
"""


def count_ambig(filename):
    ambigs = OrderedDict()
    for seq in screed.open(filename):
        seq_name = seq.name
        seq = seq.sequence.upper()
        length = len(seq)

        counter = Counter()
        for base in seq:
            counter[base] += 1

        num_non_bp = 0
        non_bases = "NX-~"
        for base_type in non_bases:
            num_non_bp += counter.get(base_type, 0)
        num_real = length - num_non_bp

        num_unambiguous_bp = 0
        unambiguous_bases = "ACGT"
        for base_type in unambiguous_bases:
            num_unambiguous_bp += counter.get(base_type, 0)

        prop_ambig = (num_real - num_unambiguous_bp) / float(num_real)

        ambigs[seq_name] = (length, prop_ambig, seq)
    return ambigs


def prop_ambig_threshold(files, threshold):
    for filename in files:
        seqs = count_ambig(filename)
        file_basename = path.splitext(filename)[0]
        new_filename = file_basename + '_processed.fasta'
        with open(new_filename, 'w') as new_file:
            for seq_name, (length, prop_ambig, seq) in seqs.items():
                if prop_ambig <= threshold:
                    print(">{}\n{}\n".format(seq_name, seq), file=new_file)


def print_prop_ambig(files):
    with open('proportion_ambiguous_sites.txt', 'w') as table_fh:
        print("Filename", "Seq_header", "Length_of_seq",
              "Proportion_ambiguous_sites", sep='\t', file=table_fh)
        for filename in files:
            all_prop_ambig = count_ambig(filename)
            for seq_name, (length, prop_ambig, seq) in all_prop_ambig.items():
                print(filename, seq_name, length, prop_ambig, sep='\t',
                      file=table_fh)


# If I am being run as a script...
if __name__ == '__main__':
    opts = docopt.docopt(CLI_ARGS)
    threshold = float(opts['-t'])
    files = opts['<FASTAFILES>']
    print_prop_ambig(files)
    if threshold is not None:
        prop_ambig_threshold(files, threshold)
