#!/usr/bin/env python
# coding=utf-8

"""Plot the word frequency against the inverse rank"""


import pandas as pd
import argparse
import csv

def main(args):
    """Run the command line program"""
    df = pd.read_csv(args.infile, header=None,
                    names=('word', 'word_frequency'))
    df['rank'] = df['word_frequency'].rank(ascending=False,
                                          method='max')
    df['inverse_rank'] = 1 / df['rank']
    ax = df.plot.scatter(x='word_frequency',
                              y='rank', loglog=True,
                              xlim=args.xlim,
                              figsize=[12, 6],
                              grid=True)
    ax.figure.savefig(args.outfile)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('infile', type=argparse.FileType('r'),
                       nargs='?', default='-',
                       help='Input file name')
    parser.add_argument('--outfile', type=str,
                       default='plotcounts.png',
                       help='Name of the output file')
    parser.add_argument('--xlim', type=float, nargs=2,
                       default=None,
                       metavar=('XMIN', 'XMAX'),
                       help='(optional) change the x-axis bounds')
    args = parser.parse_args()
    main(args)

