"""
ltbio: Luisa's bioinformatics library.
"""

from __future__ import print_function


def print_fasta(name, sequence, out_file, width=72):
    print(">", name, sep='', file=out_file)
    if width < 1:
        width = len(sequence)
    for pos in range(0, len(sequence), width):
        print(sequence[pos:pos+width], file=out_file)
