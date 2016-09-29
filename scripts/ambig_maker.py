#!/usr/bin/env python3

from __future__ import print_function
from os import path

import docopt
import sys
import screed

__author__ = "lteasnail"


CLI_ARGS = """
USAGE:
ambig_maker.py [-g FILE] [-1 FILE] [-2 FILE]

OPTIONS:
    -g FILE   gene list - i.e. the fasta headers
    -1 FILE   the h1 fasta file
    -2 FILE   the h2 fasta file

reformat fasta file from fisher script
"""


def load_fa(fafile):
    fadict = {}
    for seq in screed.open(fafile):
        fadict[seq.name] = seq.sequence
    return fadict


def make_ambig(list, h1_fasta, h2_fasta):
    h1_seqs = load_fa(h1_fasta)
    h2_seqs = load_fa(h2_fasta)
    for gene_id in list:
        seq_h1 = h1_seqs.get(gene_id, None)
        seq_h2 = h2_seqs.get(gene_id, None)
        if seq_h1 is None and seq_h2 is None:
            continue

        length = len(seq_h1)
        if len(seq_h2) != length:
            print("ERROR: The two sequence lengths differ", gene_id, h1_fasta,
                  file=sys.stderr)
            continue

        ambig = []
        for base in range(length):
            if seq_h1[base] == seq_h2[base]:
                ambig.append(seq_h1[base])
            elif seq_h1[base] != seq_h2[base]:
                if seq_h1[base] == 'C' and seq_h2[base] == 'T':
                    ambig.append('Y')
                elif seq_h1[base] == 'T' and seq_h2[base] == 'C':
                    ambig.append('Y')
                elif seq_h1[base] == 'A' and seq_h2[base] == 'G':
                    ambig.append('R')
                elif seq_h1[base] == 'G' and seq_h2[base] == 'A':
                    ambig.append('R')
                elif seq_h1[base] == 'A' and seq_h2[base] == 'T':
                    ambig.append('W')
                elif seq_h1[base] == 'T' and seq_h2[base] == 'A':
                    ambig.append('W')
                elif seq_h1[base] == 'G' and seq_h2[base] == 'C':
                    ambig.append('S')
                elif seq_h1[base] == 'C' and seq_h2[base] == 'G':
                    ambig.append('S')
                elif seq_h1[base] == 'T' and seq_h2[base] == 'G':
                    ambig.append('K')
                elif seq_h1[base] == 'G' and seq_h2[base] == 'T':
                    ambig.append('K')
                elif seq_h1[base] == 'C' and seq_h2[base] == 'A':
                    ambig.append('M')
                elif seq_h1[base] == 'A' and seq_h2[base] == 'C':
                    ambig.append('M')

        ambig_sequence = "".join(ambig)
        print(">", gene_id, "\n", ambig_sequence, sep="", file=sys.stdout)

# If I am being run as a script...
if __name__ == '__main__':
    opts = docopt.docopt(CLI_ARGS)
    gene_list = opts['-g']
    h1_fasta = opts['-1']
    h2_fasta = opts['-2']
    with open(gene_list, 'r') as fh:
        list = fh.read().splitlines()
        make_ambig(list, h1_fasta, h2_fasta)
