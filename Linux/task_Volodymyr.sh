#!/bin/bash
for run in {1..10}
do
DATE=$(date +"%d.%m.%y")
echo $run
echo $DATE
touch $run'_'$DATE
done
