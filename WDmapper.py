#Shuyu Wang

import sys
import string


for line in sys.stdin:
	line = line.strip()
	words = line.split()
	for word in words:
		new_word = word.translate(None, string.punctuation)
		new_word.replace('"', '')
		print '%s\t%s' % (new_word, 1)
