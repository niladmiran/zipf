#!/usr/bin/env python
# coding=utf-8

"""Collection of commonly used functions."""

import csv
import sys
from collections import Counter


def collection_to_csv(collection, num=None):
    """
    Write out collection of items and counts in csv format

    Parameters
    ----------------
    collection: collections.Counter()
        Collection of items and counts
    num: int
        Limit output to N most frequent items
    """
    if num is None:
        num = len(collection.most_common())
    writer = csv.writer(sys.stdout)
    writer.writerows(collection.most_common()[0:num])

