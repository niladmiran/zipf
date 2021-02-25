#!/bin/bash

# find the file with most lines under a given directory $1
# and a given extension $2

# note that we use grep to remove the total count
wc -l $1/*.$2 | sort -r | grep -v "total" | head -n 1


