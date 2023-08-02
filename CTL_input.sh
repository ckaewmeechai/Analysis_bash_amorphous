#!/bin/bash

number="-2 -1 0 +1 +2"
sum_files=CTL_Energy.txt

for i in $number ; do
     
    File_di=O_288_q$i

    grep 'ENERGY' $File_di/GaO.out | tail -1 | awk '{print $9}'  >> $sum_files
done
