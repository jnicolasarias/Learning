#!/bin/bash

echo nombre input sin extension

read input

echo nombre output

read output

cat $input.txt | tr -s '[:blank:]' ',' > $output.csv
