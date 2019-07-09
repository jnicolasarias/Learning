#!/bin/bash
python3 nums.py >> archivito.txt
grep 3 archivito.txt | wc -w


