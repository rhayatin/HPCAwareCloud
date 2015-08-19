#!/bin/bash
# shell script to open vm with assigned affinity
# to run:
#  	sh vm.sh Fedora
#	sh vm.sh Fedora 3
#	sh vm.sh Fedora 0 1
#	sh vm.sh Fedora 0 2 3
#	sh vm.sh Fedora 0 1 2 3
#
# checking the number of parameters
if [ $# -lt 1 ] || [ $# -gt 5 ]
then
	echo " Invalid Arguments "
	echo " Format:  /'sh vm.sh <VM NAME> [optional: affinities : 0-3]/'"
	exit
fi


# when only the virtual machine has been passed
if [ $# -eq 1 ]
then	
		 taskset -c 0,1 VBoxManage startvm $1 &
		 
# when affinity is set along with virtual machine
elif [ $# -eq 5 ] # 4 cores
then
		 taskset -c "$2","$3","$4","$5" setsid VBoxManage startvm $1 &
		
elif [ $# -eq 4 ] # 3 cores
then
		 taskset -c "$2","$3","$4" setsid VBoxManage startvm $1 &
elif [ $# -eq 3 ] # 2 cores
then
		 taskset -c "$2","$3" setsid VBoxManage startvm $1 &
else # 1 core
		 taskset -c "$2" setsid VBoxManage startvm $1 &
fi

exit
