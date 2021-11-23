#!/usr/bin/env bash

echo q | atop -r $1 -b $2 -e $3 > var/top.out
