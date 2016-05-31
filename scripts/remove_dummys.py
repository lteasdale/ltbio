#!/usr/bin/env python3

import screed
from ltbio import print_fasta

# Author: Luisa Teasdale

CLI_OPTIONS = """
USAGE:
remove_dummys.py <fasta_files> ...

Remove any sequences from a fasta file consisting entirely of any combination
of either '~' or '-' or 'N' or 'n'.

"""


def main(fasta_files):

    for fasta_file in fasta_files:
        out_file = fasta_file + ".remove_dummys.fas"
        out_fh = open(out_file, 'w')
        records = screed.open(fasta_file)
        for record in records:
            if len(record.sequence.strip('~-Nn')) != 0:
                print_fasta(record.name, record.sequence, out_fh)
        out_fh.close()
        records.close()

if __name__ == "__main__":
    from docopt import docopt
    opts = docopt(CLI_OPTIONS)
    main(opts['<fasta_files>'])
