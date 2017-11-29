1)SSH to ENCS
2)copy everything in a folder and make sure they have 
3)load hadoop environment >module load hadoop
4)Verify $HADOOP_DIR is poiniting to hadoop installation dir after you loaded hadoop
5)You can run the driver.py with parameters > ./driver.py <input.csv> <outputDir> <mapper.py> <reducer.py>


Here is a sample procedure and output from my encs account.

login as: a_argyro
a_argyro@login.encs.concordia.ca's password:
Last login: Sun Nov 26 20:50:34 2017 from 166-84-252-216.dsl.colba.net
==========================================================================
   Concordia University Faculty of Engineering and Computer Science

             Unauthorized access is strictly forbidden.

For assistance: e-mail: servicedesk@encs.concordia.ca
For information:   web: http://www.concordia.ca/encs/

==========================================================================
[poise] [/home/a/a_argyro] > cd ~/ass2/final/
[poise] [/home/a/a_argyro/ass2/final] > ls
driver.py  mapper.py  reducer.py
[poise] [/home/a/a_argyro/ass2/final] > module load hadoop
[poise] [/home/a/a_argyro/ass2/final] > echo $HADOOP_DIR/
/encs/pkg/hadoop-2.7.1/root/
[poise] [/home/a/a_argyro/ass2/final] > mkdir out
[poise] [/home/a/a_argyro/ass2/final] > ls
driver.py  mapper.py  out  reducer.py
[poise] [/home/a/a_argyro/ass2/final] > ll
total 16
-rwxrwx--- 1 a_argyro a_argyro 2729 Nov 27 20:05 driver.py
-rwxrwx--x 1 a_argyro a_argyro 1208 Nov 27 20:05 mapper.py
drwxrwx--- 2 a_argyro a_argyro 4096 Nov 27 20:07 out
-rwxrwx--x 1 a_argyro a_argyro 2655 Nov 27 20:06 reducer.py
[poise] [/home/a/a_argyro/ass2/final] > ./driver.py ./nms_airborne_radioactivity_ssn_radioactivite_dans_air.csv ./out/ ./mapper.py ./reducer.py
Starting MapReduce job
MapReduce job took 2.62838888168 to run
17/11/27 20:08:59 INFO Configuration.deprecation: session.id is deprecated. Instead, use dfs.metrics.session-id
17/11/27 20:08:59 INFO jvm.JvmMetrics: Initializing JVM Metrics with processName=JobTracker, sessionId=
17/11/27 20:08:59 INFO jvm.JvmMetrics: Cannot initialize JVM Metrics with processName=JobTracker, sessionId= - already initialized
17/11/27 20:08:59 INFO mapred.FileInputFormat: Total input paths to process : 1
17/11/27 20:08:59 INFO mapreduce.JobSubmitter: number of splits:1
17/11/27 20:08:59 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_local1416275773_0001
17/11/27 20:09:00 INFO mapred.LocalDistributedCacheManager: Localized file:/nfs/home/a/a_argyro/ass2/final/mapper.py as file:/tmp/hadoop-a_argyro/mapred/local/1511831340071/mapper.py
17/11/27 20:09:00 INFO mapred.LocalDistributedCacheManager: Localized file:/nfs/home/a/a_argyro/ass2/final/reducer.py as file:/tmp/hadoop-a_argyro/mapred/local/1511831340072/reducer.py
17/11/27 20:09:00 INFO mapreduce.Job: The url to track the job: http://localhost:8080/
17/11/27 20:09:00 INFO mapred.LocalJobRunner: OutputCommitter set in config null
17/11/27 20:09:00 INFO mapreduce.Job: Running job: job_local1416275773_0001
17/11/27 20:09:00 INFO mapred.LocalJobRunner: OutputCommitter is org.apache.hadoop.mapred.FileOutputCommitter
17/11/27 20:09:00 INFO output.FileOutputCommitter: File Output Committer Algorithm version is 1
17/11/27 20:09:00 INFO mapred.LocalJobRunner: Waiting for map tasks
17/11/27 20:09:00 INFO mapred.LocalJobRunner: Starting task: attempt_local1416275773_0001_m_000000_0
17/11/27 20:09:00 INFO output.FileOutputCommitter: File Output Committer Algorithm version is 1
17/11/27 20:09:00 INFO mapred.Task:  Using ResourceCalculatorProcessTree : [ ]
17/11/27 20:09:00 INFO mapred.MapTask: Processing split: file:/home/a/a_argyro/ass2/final/nms_airborne_radioactivity_ssn_radioactivite_dans_air.csv:0+2380001
17/11/27 20:09:00 INFO mapred.MapTask: numReduceTasks: 1
17/11/27 20:09:00 INFO mapred.MapTask: (EQUATOR) 0 kvi 26214396(104857584)
17/11/27 20:09:00 INFO mapred.MapTask: mapreduce.task.io.sort.mb: 100
17/11/27 20:09:00 INFO mapred.MapTask: soft limit at 83886080
17/11/27 20:09:00 INFO mapred.MapTask: bufstart = 0; bufvoid = 104857600
17/11/27 20:09:00 INFO mapred.MapTask: kvstart = 26214396; length = 6553600
17/11/27 20:09:00 INFO mapred.MapTask: Map output collector class = org.apache.hadoop.mapred.MapTask$MapOutputBuffer
17/11/27 20:09:00 INFO streaming.PipeMapRed: PipeMapRed exec [/nfs/home/a/a_argyro/ass2/final/mapper.py]
17/11/27 20:09:00 INFO Configuration.deprecation: mapred.task.id is deprecated. Instead, use mapreduce.task.attempt.id
17/11/27 20:09:00 INFO Configuration.deprecation: mapred.task.is.map is deprecated. Instead, use mapreduce.task.ismap
17/11/27 20:09:00 INFO Configuration.deprecation: mapred.skip.on is deprecated. Instead, use mapreduce.job.skiprecords
17/11/27 20:09:00 INFO Configuration.deprecation: mapred.local.dir is deprecated. Instead, use mapreduce.cluster.local.dir
17/11/27 20:09:00 INFO Configuration.deprecation: map.input.file is deprecated. Instead, use mapreduce.map.input.file
17/11/27 20:09:00 INFO Configuration.deprecation: mapred.job.id is deprecated. Instead, use mapreduce.job.id
17/11/27 20:09:00 INFO Configuration.deprecation: user.name is deprecated. Instead, use mapreduce.job.user.name
17/11/27 20:09:00 INFO Configuration.deprecation: map.input.start is deprecated. Instead, use mapreduce.map.input.start
17/11/27 20:09:00 INFO Configuration.deprecation: mapred.tip.id is deprecated. Instead, use mapreduce.task.id
17/11/27 20:09:00 INFO Configuration.deprecation: mapred.task.partition is deprecated. Instead, use mapreduce.task.partition
17/11/27 20:09:00 INFO Configuration.deprecation: map.input.length is deprecated. Instead, use mapreduce.map.input.length
17/11/27 20:09:00 INFO Configuration.deprecation: mapred.work.output.dir is deprecated. Instead, use mapreduce.task.output.dir
17/11/27 20:09:00 INFO streaming.PipeMapRed: R/W/S=1/0/0 in:NA [rec/s] out:NA [rec/s]
17/11/27 20:09:00 INFO streaming.PipeMapRed: R/W/S=10/0/0 in:NA [rec/s] out:NA [rec/s]
17/11/27 20:09:00 INFO streaming.PipeMapRed: R/W/S=100/0/0 in:NA [rec/s] out:NA [rec/s]
17/11/27 20:09:00 INFO streaming.PipeMapRed: Records R/W=891/1
17/11/27 20:09:00 INFO streaming.PipeMapRed: R/W/S=1000/120/0 in:NA [rec/s] out:NA [rec/s]
17/11/27 20:09:00 INFO streaming.PipeMapRed: R/W/S=10000/9298/0 in:NA [rec/s] out:NA [rec/s]
17/11/27 20:09:00 INFO streaming.PipeMapRed: MRErrorThread done
17/11/27 20:09:00 INFO streaming.PipeMapRed: mapRedFinished
17/11/27 20:09:00 INFO mapred.LocalJobRunner:
17/11/27 20:09:00 INFO mapred.MapTask: Starting flush of map output
17/11/27 20:09:00 INFO mapred.MapTask: Spilling map output
17/11/27 20:09:00 INFO mapred.MapTask: bufstart = 0; bufend = 407913; bufvoid = 104857600
17/11/27 20:09:00 INFO mapred.MapTask: kvstart = 26214396(104857584); kvend = 26151540(104606160); length = 62857/6553600
17/11/27 20:09:00 INFO mapred.MapTask: Finished spill 0
17/11/27 20:09:00 INFO mapred.Task: Task:attempt_local1416275773_0001_m_000000_0 is done. And is in the process of committing
17/11/27 20:09:00 INFO mapred.LocalJobRunner: Records R/W=891/1
17/11/27 20:09:00 INFO mapred.Task: Task 'attempt_local1416275773_0001_m_000000_0' done.
17/11/27 20:09:00 INFO mapred.LocalJobRunner: Finishing task: attempt_local1416275773_0001_m_000000_0
17/11/27 20:09:00 INFO mapred.LocalJobRunner: map task executor complete.
17/11/27 20:09:00 INFO mapred.LocalJobRunner: Waiting for reduce tasks
17/11/27 20:09:00 INFO mapred.LocalJobRunner: Starting task: attempt_local1416275773_0001_r_000000_0
17/11/27 20:09:00 INFO output.FileOutputCommitter: File Output Committer Algorithm version is 1
17/11/27 20:09:00 INFO mapred.Task:  Using ResourceCalculatorProcessTree : [ ]
17/11/27 20:09:00 INFO mapred.ReduceTask: Using ShuffleConsumerPlugin: org.apache.hadoop.mapreduce.task.reduce.Shuffle@446dcf38
17/11/27 20:09:00 INFO reduce.MergeManagerImpl: MergerManager: memoryLimit=360395552, maxSingleShuffleLimit=90098888, mergeThreshold=237861072, ioSortFactor=10, memToMemMergeOutputsThreshold=10
17/11/27 20:09:00 INFO reduce.EventFetcher: attempt_local1416275773_0001_r_000000_0 Thread started: EventFetcher for fetching Map Completion Events
17/11/27 20:09:00 INFO reduce.LocalFetcher: localfetcher#1 about to shuffle output of map attempt_local1416275773_0001_m_000000_0 decomp: 439345 len: 439349 to MEMORY
17/11/27 20:09:00 INFO reduce.InMemoryMapOutput: Read 439345 bytes from map-output for attempt_local1416275773_0001_m_000000_0
17/11/27 20:09:00 INFO reduce.MergeManagerImpl: closeInMemoryFile -> map-output of size: 439345, inMemoryMapOutputs.size() -> 1, commitMemory -> 0, usedMemory ->439345
17/11/27 20:09:00 INFO reduce.EventFetcher: EventFetcher is interrupted.. Returning
17/11/27 20:09:00 INFO mapred.LocalJobRunner: 1 / 1 copied.
17/11/27 20:09:00 INFO reduce.MergeManagerImpl: finalMerge called with 1 in-memory map-outputs and 0 on-disk map-outputs
17/11/27 20:09:00 INFO mapred.Merger: Merging 1 sorted segments
17/11/27 20:09:00 INFO mapred.Merger: Down to the last merge-pass, with 1 segments left of total size: 439332 bytes
17/11/27 20:09:00 INFO reduce.MergeManagerImpl: Merged 1 segments, 439345 bytes to disk to satisfy reduce memory limit
17/11/27 20:09:00 INFO reduce.MergeManagerImpl: Merging 1 files, 439349 bytes from disk
17/11/27 20:09:00 INFO reduce.MergeManagerImpl: Merging 0 segments, 0 bytes from memory into reduce
17/11/27 20:09:00 INFO mapred.Merger: Merging 1 sorted segments
17/11/27 20:09:00 INFO mapred.Merger: Down to the last merge-pass, with 1 segments left of total size: 439332 bytes
17/11/27 20:09:00 INFO mapred.LocalJobRunner: 1 / 1 copied.
17/11/27 20:09:00 INFO streaming.PipeMapRed: PipeMapRed exec [/nfs/home/a/a_argyro/ass2/final/reducer.py]
17/11/27 20:09:00 INFO Configuration.deprecation: mapred.job.tracker is deprecated. Instead, use mapreduce.jobtracker.address
17/11/27 20:09:00 INFO Configuration.deprecation: mapred.map.tasks is deprecated. Instead, use mapreduce.job.maps
17/11/27 20:09:00 INFO streaming.PipeMapRed: R/W/S=1/0/0 in:NA [rec/s] out:NA [rec/s]
17/11/27 20:09:00 INFO streaming.PipeMapRed: R/W/S=10/0/0 in:NA [rec/s] out:NA [rec/s]
17/11/27 20:09:00 INFO streaming.PipeMapRed: R/W/S=100/0/0 in:NA [rec/s] out:NA [rec/s]
17/11/27 20:09:00 INFO streaming.PipeMapRed: R/W/S=1000/0/0 in:NA [rec/s] out:NA [rec/s]
17/11/27 20:09:00 INFO streaming.PipeMapRed: Records R/W=5442/1
17/11/27 20:09:00 INFO streaming.PipeMapRed: R/W/S=10000/122/0 in:NA [rec/s] out:NA [rec/s]
17/11/27 20:09:00 INFO streaming.PipeMapRed: MRErrorThread done
17/11/27 20:09:00 INFO streaming.PipeMapRed: mapRedFinished
17/11/27 20:09:00 INFO mapred.Task: Task:attempt_local1416275773_0001_r_000000_0 is done. And is in the process of committing
17/11/27 20:09:00 INFO mapred.LocalJobRunner: 1 / 1 copied.
17/11/27 20:09:00 INFO mapred.Task: Task attempt_local1416275773_0001_r_000000_0 is allowed to commit now
17/11/27 20:09:00 INFO output.FileOutputCommitter: Saved output of task 'attempt_local1416275773_0001_r_000000_0' to file:/nfs/home/a/a_argyro/ass2/final/out/_temporary/0/task_local1416275773_0001_r_000000
17/11/27 20:09:00 INFO mapred.LocalJobRunner: Records R/W=5442/1 > reduce
17/11/27 20:09:00 INFO mapred.Task: Task 'attempt_local1416275773_0001_r_000000_0' done.
17/11/27 20:09:00 INFO mapred.LocalJobRunner: Finishing task: attempt_local1416275773_0001_r_000000_0
17/11/27 20:09:00 INFO mapred.LocalJobRunner: reduce task executor complete.
17/11/27 20:09:01 INFO mapreduce.Job: Job job_local1416275773_0001 running in uber mode : false
17/11/27 20:09:01 INFO mapreduce.Job:  map 100% reduce 100%
17/11/27 20:09:01 INFO mapreduce.Job: Job job_local1416275773_0001 completed successfully
17/11/27 20:09:01 INFO mapreduce.Job: Counters: 30
        File System Counters
                FILE: Number of bytes read=5858592
                FILE: Number of bytes written=2129102
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
        Map-Reduce Framework
                Map input records=15716
                Map output records=15715
                Map output bytes=407913
                Map output materialized bytes=439349
                Input split bytes=136
                Combine input records=0
                Combine output records=0
                Reduce input groups=245
                Reduce shuffle bytes=439349
                Reduce input records=15715
                Reduce output records=245
                Spilled Records=31430
                Shuffled Maps =1
                Failed Shuffles=0
                Merged Map outputs=1
                GC time elapsed (ms)=0
                Total committed heap usage (bytes)=1029701632
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
        File Input Format Counters
                Bytes Read=2380001
        File Output Format Counters
                Bytes Written=16469
17/11/27 20:09:01 INFO streaming.StreamJob: Output directory: /nfs/home/a/a_argyro/ass2/final/out

MapReduce job ended, fetching processed data
Please enter a year:
2017
Please enter a location:
Montreal
The Maximum value of the metric 7Be MDC/7Be CMD (mBq/m3) for the location Montreal in the year 2017 is 0.054468434
The Minimum value of the metric 7Be MDC/7Be CMD (mBq/m3) for the location Montreal in the year 2017 is 0.012970821
The Median value of the metric 7Be MDC/7Be CMD (mBq/m3) for the location Montreal in the year 2017 is 0.031974585
The Standard Deviation value of the metric 7Be MDC/7Be CMD (mBq/m3) for the location Montreal in the year 2017 is 0.0126136644716
Please enter a year:
2017
Please enter a location:
Winnipeg
The Maximum value of the metric 7Be MDC/7Be CMD (mBq/m3) for the location Winnipeg in the year 2017 is 0.039384817
The Minimum value of the metric 7Be MDC/7Be CMD (mBq/m3) for the location Winnipeg in the year 2017 is 0.012894415
The Median value of the metric 7Be MDC/7Be CMD (mBq/m3) for the location Winnipeg in the year 2017 is 0.030439521
The Standard Deviation value of the metric 7Be MDC/7Be CMD (mBq/m3) for the location Winnipeg in the year 2017 is 0.00798057842002
