#!/bin/bash

number=" -2 -1 0 +1 +2"

basis_file=BASIS_MOLOPT
potential_file=POTENTIAL
basis_admm=BASIS_ADMM_MOLOPT
template_file=GaO_temp.inp
input_file=GaO.inp
short=short_2.pbs
std=std_2.pbs
wfn_file=GaO-RESTART.wfn

input_dir=/work/e05/e05/ucapcka/Ov-a-Ga2O3/Ov_CN2/O_temp

for i in $number ; do
    work_dir=Energy_q${i}
    name_dir=/Ov_CN2/O_166/O_288_q${i}
    wfn_dir=/work/e05/e05/ucapcka/Ov-a-Ga2O3$name_dir
    if [ ! -d $work_dir ] ; then
        mkdir $work_dir
    else
        rm -r $work_dir/*
    fi
    line=${i}

    tail -401 $wfn_dir/GaO-pos-1.xyz > $work_dir/GaO.xyz
    sed -e "s/CHARGEq/$i/g" \
        $input_dir/$template_file > $work_dir/$input_file
    cp  $wfn_dir/$basis_file $work_dir
    cp  $wfn_dir/$basis_admm $work_dir
    cp  $wfn_dir/$potential_file $work_dir
    cp  $input_dir/$short $work_dir
    cp  $input_dir/$std $work_dir
    cp  $wfn_dir/$wfn_file $work_dir
    cp /work/e05/e05/ucapcka/Charge/bader $work_dir
done
