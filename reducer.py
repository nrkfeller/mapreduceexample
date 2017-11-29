#!/usr/bin/env python

# Reducer using Python iterators and generators
# based on [4] from page 93 of lecture slides ch-5-mapreduce-part1.pdf

__author__ = "Nicolas Feller"

from itertools import groupby
from operator import itemgetter
import sys
import math

def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator,1)
    
def median(x):
    #Input: list of numbers; Output: the "middle" number of the ordered list
    sorted_x = sorted(x)
    length_n = len(x)
    middle = length_n // 2 #Integer division
    
    #Even numbered amount in list:
    if length_n % 2 ==0:
        median_even = (sorted_x[middle-1] + sorted_x[middle])/2
        return(median_even) # Remember index 0 as 1st element.
    else:
        return(sorted_x[middle]) # Return middle number
     
def mean(x):
    #Input: list of numbers; Output: the "mean/average" of the list
    return sum(x)/len(x)

def variance(x):
    n = len(x)
    x_bar = mean(x)
    return(sum((x_i-x_bar)**2 for x_i in x)/(n-1))

def stdev(x):
    return(math.sqrt(variance(x)))
                  
def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)
    # Group locationYear and 7BeMDC into 'group'
    # Since MapReduce is a distributed process, each locationYear
    # may have multiple 7BeMDCs. 'group' will have all 7Be MDCs
    # which can be retrieved using the locationYear as the key.
    for locationYear, group in groupby(data, itemgetter(0)):
        try:
            # For each locationYear, pull the 7Be MDC(s) for the locationYear
            # from 'group' and create a list (in-memory accumulation) of all 7Be MDC(s).
            # The reducer reads each each locationYear output by the mapper, looks it up
            # in the list of locationYear groups it compiles, and passes the entire iterator result
            # to a list constructor beacause multiple opperations are needed on each stripe of data.
            data_7BeMDC = list((float(beryllium) for locationYear, beryllium in group))
            max_7BeMDC = str(max(data_7BeMDC))
            min_7BeMDC = str(min(data_7BeMDC))
            median_7BeMDC = str(median(data_7BeMDC))
            stdev_7BeMDC = str(stdev(data_7BeMDC))
            # Write to stdout
            print "%s%s%s%s%s%s%s%s%s" %(locationYear,separator,max_7BeMDC,separator,min_7BeMDC,separator,median_7BeMDC,separator,stdev_7BeMDC)
        except ValueError:
            # beryllium (7Be MDC) was not a number, so do nothing
            pass
        
if __name__ == "__main__":
    main()

            
        
