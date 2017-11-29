#!/usr/bin/env python

__author__ = "Nicolas Feller"

import sys
import os
import subprocess
from collections import defaultdict
import csv 
import time

if __name__ == '__main__':
    
    print "Starting MapReduce job"
    
    """
    Expected arguments: SOURCE_FILE DESTINATION_DIR MAPPER REDUCER
    """
    source_file = os.path.abspath(sys.argv[1])
    dest_file = os.path.abspath(sys.argv[2])
    mapper = os.path.abspath(sys.argv[3])
    reducer = os.path.abspath(sys.argv[4])

    subprocess.Popen("rm -rf " + dest_file, shell=True,executable="/bin/bash", stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    cmd = "hadoop jar $HADOOP_DIR/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -files " + mapper + "," +reducer + " -mapper " + mapper + " -reducer " + reducer + " -input " + source_file + " -output " + dest_file
    start_time = time.time()
    output,error = subprocess.Popen(cmd, shell=True, executable="/bin/bash", stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    print "MapReduce job took", time.time() - start_time, "to run"
    print error
    outFile = os.path.abspath(sys.argv[2]+'/part-00000')
    
    print "MapReduce job ended, fetching processed data"
    
    processed_data = open(outFile, 'rb')
    data = csv.reader(processed_data, delimiter='\t')
    output_data = defaultdict(list)
    
    for column in data:
        cityYear = column[0]
        maximum = column[1]
        minimum = column[2]
        median_value = column[3]
        stdev = column[4]
        output_data[cityYear].append(maximum)
        output_data[cityYear].append(minimum)
        output_data[cityYear].append(median_value)
        output_data[cityYear].append(stdev)
    try:
        while(1):
            usr_input = raw_input('Please enter a year: \n')
            if usr_input =='':
                sys.exit()
            year = usr_input
            city = raw_input('Please enter a location: \n')
            key = city + ',' + year
            results = output_data[key]
            print "The Maximum value of the metric 7Be MDC/7Be CMD (mBq/m3) for the location " + city + " in the year " + year + " is " +str(results[0])
            print "The Minimum value of the metric 7Be MDC/7Be CMD (mBq/m3) for the location " + city + " in the year " + year + " is " +str(results[1])
            print "The Median value of the metric 7Be MDC/7Be CMD (mBq/m3) for the location " + city + " in the year " + year + " is " +str(results[2])
            print "The Standard Deviation value of the metric 7Be MDC/7Be CMD (mBq/m3) for the location " + city + " in the year " + year + " is " +str(results[3])
    except ValueError:
        print "That was not a valid entry. Please try again."
