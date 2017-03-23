#Shuyu Wang

import sys
import string

current_word = None
current_count = 0
word = None

for line in sys.stdin:
	line = line.strip()

	#parse the input we got from WDmapper.py	
	word, count = line.split('\t', 1)
	
	#convert count (a string) into int	
	try:
		count = int(count)
	except ValueError:
		#if count was not a number, silently ignore the line
		continue
	
	#Hadoop sorts map output by key (here word) before it
	# is passed to the reducer

	if current_word == word:
		current_count += count
	else:
		if current_word:
			print '%s\t%s' % (current_word, current_count)
		current_count = count
		current_word = word

#output the last word if needed!
if current_word == word:
	print '%s\t%s' % (current_word, current_count)

