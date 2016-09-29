#!/usr/bin/env python3

# Tree_renamer!

from __future__ import print_function
from os import path
from ete3 import Tree
import docopt
import sys


__author__ = "lteasnail"

CLI_ARGS = """
USAGE:
tree_renamer.py -f TREEFILE -n NAMES

OPTIONS:
 -f TREEFILE    The tree file in newick format.
 -n NAMES       Tab delimited file with names to find in the first column and
                names to replace them with in the second.

This script replaces the tip labels in a tree.

"""

# This function processes the list of original and new names.


def get_name_replacer(names_file):
    replacer = {}
    with open(names_file) as fh:
        for line in fh:
            orig, new = line.strip().split("\t")
            replacer[orig] = new
    return replacer

# This function replaces the original names with the new names and returns the
# tree in nemick format.


def replace_names(tree_file, replacer):
    tree = Tree(tree_file)
    errored = False
    for tip in tree.iter_leaves():
        try:
            newname = replacer[tip.name.strip("'")]
            tip.name = newname
        except KeyError as exc:
            print("ERROR: Tip is missing from replacement file: '{}'".format(
                  tip.name), file=sys.stderr)
            errored = True
    return tree.write()


# If I am being run as a script...s
if __name__ == '__main__':
    opts = docopt.docopt(CLI_ARGS)
    names_file = opts['-n']
    tree_file = opts['-f']
    replacer = get_name_replacer(names_file)
    print(replace_names(tree_file, replacer), file=sys.stdout)
    print('Finished!', file=sys.stderr)
