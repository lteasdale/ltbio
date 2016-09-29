#!/usr/bin/env python

# Seq_chopper!

from __future__ import print_function
from os import path
# The fasta parser.
import screed
import docopt
import sys


__author__ = "Luisa Teasdale"

CLI_ARGS = """
USAGE:
seq_chopper.py -f SEQFILE -p PARTITIONS

OPTIONS:
 -f SEQFILE     The fasta file containing all sequences to be chopped.
 -p PARTITIONS  Partition file which contains the sections of the alignment you
                want chopped out and the name of the fasta file the subset will
                be printed to.

"""

# Function to process the partitions file


def sum_partitions(line):
    name = line.strip().split(' ')[0]
    start_pos = line.strip().split(' ')[2]
    end_pos = line.strip().split(' ')[4]
    return name, start_pos, end_pos


# Function to do the chopping


def chop_seqs(fastafile, name, start_pos, end_pos, exon_no):
    with screed.open(fastafile) as fh:
        for seq in fh:
            if seq.name == name:
                seq_name = seq.name + '_' + str(exon_no)
                seq = seq.sequence
                start = int(start_pos) - 1
                end = int(end_pos)
                subset = seq[start:end]
                print(">{}\n{}".format(seq_name, subset), file=sys.stdout)


# If I am being run as a script...
if __name__ == '__main__':
    opts = docopt.docopt(CLI_ARGS)
    partitionfile = opts['-p']
    fastafile = opts['-f']
    partitions = open(partitionfile)
    print(fastafile, file=sys.stderr)
    exon_no = 0
    for line in partitions:
        exon_no += 1
        name, start_pos, end_pos = sum_partitions(line)
        chop_seqs(fastafile, name, start_pos, end_pos, exon_no)
        print('chopped partition {}'.format(name), file=sys.stderr)
    print('Finished!', file=sys.stderr)
