#!/usr/bin/env python
# coding=utf-8

"""List the files in a given directory with a given suffix"""

import argparse
import glob
import sys

def main(args):
    """Run the command line program"""
    files = glob.glob(args.dir + '*.' + args.suffix)
    for term in files:
        print(term)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('dir', type=str, default='-',
                       help='Directory')
    parser.add_argument('suffix', type=str,
                       help='File suffix (e.g. py, sh)')
    args = parser.parse_args()
    main(args)
