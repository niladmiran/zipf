#!/bin/bash

# print a list of the unique publish years of the files that
# takes
for file in $@
do
    echo $file
    cut -d, -f 2 $file | sort | uniq
done
