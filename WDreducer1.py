#Shuyu Wang
#sw883

import sys
import operator

word_count = {}
num_word = 0

for line in sys.stdin:
    line = line.strip()

    # parse the input we got from WDmapper1.py
    word, count = line.split('\t', 1)

    # convert count (a string) to int
    try:
        count = int(count)
    except ValueError:
	#if count was not a number, silently ignore the line
	continue
	
    # hadoop sorts map output by key (here: word) before ut
    # is passed to the reducer

