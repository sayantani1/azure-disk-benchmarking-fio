import subprocess
import sys
import re
from operator import itemgetter

maxIOPS=[]
maxBW=[]

def grep_func(search,inp):
    for line in inp:
        if search in line:
            return line

def max_iops(ave_iops):
    maxIOPS.append(ave_iops)
    return

def max_bw(ave_bw):
    maxBW.append(ave_bw)
    return

def main():

  iodepth=[8,16,32,64,128,256]
  bs=[8,16,32,64,128,256]
  fio_filename=sys.argv[1]
  run_time=5 #Runtime in seconds

    for i in bs:
        for j in iodepth:
            temp1=[]
            temp2=[]
            cmd='fio --runtime='+str(run_time)+' '+fio_filename+' --bs='+str(i)+'k --iodepth='+str(j)
            fio_out=subprocess.check_output(cmd, shell=True).rstrip().split('\n')
        
            ave_iops=float(grep_func('iops',fio_out).split(',')[2].split('=')[1])
            ave_bw=float(grep_func('bw',fio_out).split(',')[3].split('=')[1])/1000
           
            print "bs="+str(i)+", iodepth="+str(j)+", ave_IOPS="+str(ave_iops)+", ave_BW="+str(ave_bw)

            temp1.append("bs="+str(i))
            temp1.append("iodepth="+str(j))
            temp1.append(ave_iops)
            max_iops(temp1)

            temp2.append("bs="+str(i))
            temp2.append("iodepth="+str(j))
            temp2.append(round(ave_bw,2))
            max_bw(temp2)
     
        print "\n"

    #Sort based on ave. iops
    maximumIOPS=sorted(maxIOPS,key=itemgetter(2))
    #Sort based on ave. throughput
    maximumBW=sorted(maxBW,key=itemgetter(2))

    #Printing the combination of bs and iodepth that gives the highest iops
    print "\nCombination of bs and iodepth that gives the highest IOPS:"
    print maximumIOPS[-1:]
    print "\nCombination of bs and iodepth that gives the highest BW:"
    print maximumBW[-1:]

if __name__== "__main__":
    main()

