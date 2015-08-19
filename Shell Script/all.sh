#!/bin/sh

taskset -c 0,1	/usr/lib/virtualbox/VirtualBox -comment Fedora -startvm cd93681a-803e-4758-8b42-bc2bac9f6cb0 |
taskset -c 2,3	/usr/lib/virtualbox/VirtualBox -comment OpenSuse -startvm a5300325-059a-427e-9e7f-103ad924577c |
taskset -c 1,2	/usr/lib/virtualbox/VirtualBox -comment Mint -startvm 371d0660-372d-4098-9681-99d3bab1194e |
taskset -c 0,3 	/usr/lib/virtualbox/VirtualBox -comment Cent -startvm 8e88108e-c22e-4756-a6dd-51b319ab542e 

