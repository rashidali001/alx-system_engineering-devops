#!/usr/bin/env bash
c=$(ls)
for list in $c;
do
item=$list
echo "$list" | cut -d "-" -f2
done
