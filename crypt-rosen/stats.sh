#!/bin/bash

echo "0 Note subtract 10 from this answer"
cat $1 | grep 0 | wc -l 
for i in `seq 1 12`
do
    echo "$i: "
    cat $1 | grep $i | wc -l
done