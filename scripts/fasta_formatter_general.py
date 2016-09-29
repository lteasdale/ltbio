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
fasta_formater_general.py <FASTAFILES>...

reformat fasta file output from fasta fisher script
"""


def reformat(fastafiles):
    exon_dict = defaultdict(list)
    for fasta_file in fastafiles:
        species_string = fasta_file.split("_phylogene")
        species = species_string[0]
        seqs = screed.open(fasta_file)
        for seq in seqs:
            exon = seq.name
            seq_name = species
            seq_sequence = seq.sequence
            sequence = (seq_name, seq.sequence)
            exon_dict[exon].append(sequence)
    return exon_dict


# If I am being run as a script...

if __name__ == '__main__':
    opts = docopt.docopt(CLI_ARGS)
    fasta_files = opts['<FASTAFILES>']
    exon_dict = reformat(fasta_files)
    for key, item in sorted(exon_dict.items()):
        exon_file_name = key + ".fas"
        with open(exon_file_name, 'w') as exon_file:
            for seq in item:
                name = seq[0]
                sequence = seq[1]
                print(">" + name + "\n" + sequence, file=exon_file)
