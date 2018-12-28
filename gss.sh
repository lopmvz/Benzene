##!/bin/bash

for i in *txt
do
#python2 ~/Workdir/ammonia/read.py  ${i} > ${i}.txt
#if [ -s "${i}.txt" ]
#then
python ~/Workdir/Benzene/Benzene/gaussian.py ${i}.txt > ${i}.dat
#fi
done
