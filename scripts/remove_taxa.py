#!/usr/bin/env python3

import screed
from ltbio import print_fasta

# Author: Luisa Teasdale and Kevin Murray

CLI_OPTIONS = """
USAGE:
remove_taxa.py [-k] <header_list> <fasta_files> ...

OPTIONS:
    -k   Keep taxa in HEADER_LIST, instead of removing them [default: False].

Remove any sequences from each FASTA file if it's name exists in <header_list>.

Doesn't need to be an exact match so be careful!!
"""


def main(header_file, fasta_files, keep=False):
    # get list of patterns to match
    headers = []
    with open(header_file) as fh:
        for header in fh:
            headers.append(header.strip())

    for fasta_file in fasta_files:
        out_file = fasta_file + "_remove_taxa.fasta"
        out_fh = open(out_file, 'w')
        records = screed.open(fasta_file)
        for record in records:
            if keep:
                for header in headers:
                    if record.name.find(header) >= 0:
                        print_fasta(record.name, record.sequence, out_fh)
            else:
                for header in headers:

                    if record.name.find(header) >= 0:
                        break
                else:
                    print_fasta(record.name, record.sequence, out_fh)
        out_fh.close()
        records.close()

if __name__ == "__main__":
    from docopt import docopt
    opts = docopt(CLI_OPTIONS)
    main(opts['<header_list>'], opts['<fasta_files>'], keep=opts['-k'])
