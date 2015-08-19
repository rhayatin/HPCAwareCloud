import os
import re
import subprocess
import psutil
import multiprocessing
import sys

CPUs = [1,3]
CPUc = [0,2]
CPU_list = [CPUs,CPUc]

vm_name = sys.argv[1]
cpu_required = sys.argv[2]
stg = "Storage"
com = "Compute"

def check_cpu_free(CPU_LIST):

    number_of_cores = psutil.cpu_count()
    current_affinity_list = psutil.Process(os.getpid()).get_cpu_affinity()
    CPU_usage_list = psutil.cpu_percent(interval = 1, percpu=True);
    least_usage_value = 30.0
    j = 0
    free_cpu = []
    for i in range(0,number_of_cores):
        if CPU_usage_list[i] <= least_usage_value:
            free_cpu.append(i)
            j = j+1

    if set(CPU_LIST).issubset(free_cpu):
        return 1
    return 0



vmt = " "
if cpu_required == com :
    if check_cpu_free(CPUc):
        vmt = ' '.join(str(e) for e in CPUc)
    elif check_cpu_free(CPUs):
        vmt = ' '.join(str(e) for e in CPUs)
    else:
        print "No CPU is free"
        while (not check_cpu_free(CPUc)) and (not check_cpu_free(CPUs)):
            print "waiting for CPUs to be released"
        #call back
else:
    if check_cpu_free(CPUs):
        vmt = ' '.join(str(e) for e in CPUs)
    elif check_cpu_free(CPUs):
        vmt = ' '.join(str(e) for e in CPUc)
    else :
        while (not check_cpu_free(CPUs)) and (not check_cpu_free(CPUc)) :
            print "waiting for CPUs to be released"
        #callback



bashcmd = "sh vm.sh " + vm_name + " " + vmt


os.system(bashcmd) #open shell script
