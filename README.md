# Benchmark Azure Disks

disk-benchmarking.py runs fio tests based on the .ini file provided for different combinations of bs and iodepth and outputs:
 - the combination of bs and iodepth that provides maximum IOPS
 - the combination of bs and iodepth that provides maximum throughput (MBps) 

The repo contains 3 ini files:
------------------------------

- fio-write.ini           - To test write throughput
- fio-read.ini            - To test read throughput
- fio-read-write.ini      - To test read, write throughput 

Update the directory parameter in the ini files to point to the directory to which the disk you are benchmarking is mounted.

To execute the code, enter the following:
-----------------------------------------
python disk-benchmarking.py ini-file-name
  
Example:
--------

python disk-benchmarking.py fio-write.ini


  
  
