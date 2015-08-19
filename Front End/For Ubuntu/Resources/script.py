import os
import psutil
import sys

CPUs = [1,3]
CPUc = [0,2]
CPU_list = [CPUs,CPUc,0,1,2,3]

vm_name = sys.argv[1]
cpu_required = sys.argv[2]
stg = "Storage"
com = "Compute"

def check_cpu_free(CPU_LIST):
    number_of_cores = psutil.cpu_count()
    CPU_usage_list = psutil.cpu_percent(interval = 1, percpu=True);
    print CPU_usage_list
    least_usage_value = 15.0
    j = 0
    free_cpu = []
    for i in range(0,number_of_cores):
        if CPU_usage_list[i] <= least_usage_value:
            free_cpu.append(i)
            j = j+1

    if set(CPU_LIST).issubset(free_cpu):
        return 1
    return 0

def no_free_cpu():
    print "No CPU is free"
    while (not check_cpu_free(CPUc)) and (not check_cpu_free(CPUs)):
        print "waiting for CPUs to be released"
    str2 = assign_free_cpu()
    return str2

def build_affinity_string(CPU_LIST):
    return ' '.join(str(e) for e in CPU_LIST)


def assign_free_cpu():
    str1 = "  "
    if cpu_required == com :
        print "Compute is required"
        if check_cpu_free(CPUc):
            print "Compute CPUs are available.. Assigning the VM to Compute CPUs"
            str1 = build_affinity_string(CPUc)
        elif check_cpu_free(CPUs):
            print "Compute CPUs are not free.. Assigning the VM to Storage CPUs"
            str1 = build_affinity_string(CPUs)
        else:
            str1 = no_free_cpu()
    elif cpu_required == stg :
        print "Storage is required"
        if check_cpu_free(CPUs):
            print "Storage CPUs are available.. Assigning the VM to Storage CPUs"
            str1 = build_affinity_string(CPUs)
        elif check_cpu_free(CPUs):
            print "Storage CPUs are not free.. Assigning the VM to Compute CPUs"
            str1 = build_affinity_string(CPUc)
        else :
            str1 = no_free_cpu()
    else:
        print "Request Error"

    return str1


vmt = " " + assign_free_cpu()
bashcmd = "sh vm.sh " + vm_name + vmt
print bashcmd
print " "
os.system(bashcmd) #open shell script
