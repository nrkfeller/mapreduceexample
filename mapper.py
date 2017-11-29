#!/usr/bin/env python

# Mapper using Python iterators and generators
# based on [4] from page 93 of lecture slides ch-5-mapreduce-part1.pdf

__author__ = "Nicolas Feller"

import sys

def read_input(file):
    for line in file:
       # split input line into values
        yield line.split(',')

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    # Process each value returned from read_input
    for values in data:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the <key,value> pair is constructed
        # as <locationYear,7Be MDC>
        try:
            location = values[0]
            if location == 'Location/Emplacement':
                continue
            year = values[2].split('-')[0]
            key = location + ',' + year
            beryllium  = values[7]
            if beryllium != '':
                print '%s%s%s' % (key, separator, beryllium)
        except ValueError:
            continue
        
if __name__ == "__main__":
    main()
                
            
