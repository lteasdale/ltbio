#!/usr/bin/env python

# This script was originally writtern by Nathan Whelan as stated below however
# the original script did not appear to work and here it has been edited by
# Kevin Murray so that it runs.

###############################################################################
# This script was written by Nathan Whelan.
# THIS SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE CONTRIBUTORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF
# OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS WITH THE
# SOFTWARE.
###############################################################################
##############################################################################
# This script will create a list of alignments sorted by evolutionary rate
# as measured by tree length divided by taxa.
# THIS SHOULD BE EXECUTED IN A FOLDER WITH SINGLE GENE TREES. As written works
# with RAxML_bestTree tree files.
# If your alignments had different format than change variable directly below
##############################################################################

from __future__ import division, print_function

import dendropy
import os
import glob
import docopt

CLI = """
USAGE:
    evorate.py [-o OUT -r] <trees> ...

OPTIONS:
    -o OUT      Output file name [default: evolRatesOrdered.txt]
    -r          Reverse sorting order (i.e. sort fastest to slowest)
"""


def evolRate(tree):
    """Function that returns evol rate for a dendropy.Tree object."""
    tree_length = tree.length()
    numberOfTaxa = len(tree.leaf_nodes())
    return(tree_length/numberOfTaxa)


def main(infiles, outfile, reverse=False):
    """Goes through each tree and calculates its evolutionary rate, sorts trees
    by rate and outputs a table of trees and ratesself."""
    ratesDict = {}

    # Read all tree rates
    for infile in infiles:
        with open(infile) as tfh:
            myTree = dendropy.Tree.get(file=tfh, schema="newick")
        ratesDict[infile] = evolRate(myTree)

    ratesList = sorted(ratesDict.items(), key=lambda x: x[1], reverse=reverse)

    with open(outfile, "w") as outf:
        # Old file will be overwritten if it exists
        for aln, rate in ratesList:
            print(aln, rate, sep='\t', file=outf)


if __name__ == "__main__":
    from docopt import docopt
    opts = docopt(CLI)
    main(opts['<trees>'], opts['-o'], opts['-r'])
