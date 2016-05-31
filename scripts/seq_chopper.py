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
 -f SEQFILE     The multi-species alignment file in fasta format.
 -p PARTITIONS  Partition file which contains the sections of the alignment you
                want chopped out and the name of the fasta file the subset will
                be printed to.

This script takes a supermatrix alignment and a text file specifying
partitions in RAxML format and will output a seperate fasta file for each
partition. At the moment the script only works with one data block per
partition.

"""

# Function to process the partitions file


def sum_partitions(line):
    name = line.strip().split(' ')[0]
    start_pos = line.strip().split(' ')[2]
    end_pos = line.strip().split(' ')[4]
    return name, start_pos, end_pos


# Function to do the chopping


def chop_seqs(fastafile, name, start_pos, end_pos):
    filename = name + '.fasta'
    with screed.open(fastafile) as fh:
        with open(filename, 'w') as newfh:
            for seq in fh:
                seq_name = seq.name
                seq = seq.sequence
                start = int(start_pos) - 1
                end = int(end_pos)
                subset = seq[start:end]
                print(">{}\n{}".format(seq_name, subset), file=newfh)


# If I am being run as a script...
if __name__ == '__main__':
    opts = docopt.docopt(CLI_ARGS)
    partitionfile = opts['-p']
    fastafile = opts['-f']
    partitions = open(partitionfile)
    print(fastafile, file=sys.stderr)
    for line in partitions:
        name, start_pos, end_pos = sum_partitions(line)
        chop_seqs(fastafile, name, start_pos, end_pos)
        print('chopped partition {}'.format(name), file=sys.stderr)
    print('Finished!', file=sys.stderr)
