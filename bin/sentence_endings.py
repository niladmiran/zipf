#!/usr/bin/env python
# coding=utf-8

"""Counter the occurrence of full stops, question marks and exaclamation"""

import sys
import argparse
from collections import Counter

def main(args):
    text = args.infile.read()
    end_counter = Counter()
    for end in ['.', '?', '!']:
        end_counter[end] += text.count(end)

    for end, cnt in end_counter.items():
        print('Number of ', end, 'is', cnt)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('infile', type=argparse.FileType('r'),
                        nargs='?',
                        default='-', help='Input file name')

    args = parser.parse_args()

    main(args)

