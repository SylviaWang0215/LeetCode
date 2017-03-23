#Shuyu Wang

import sys
import string
import operator

line_num = 0
words_num = 0
words_count = {}

for line in sys.stdin:
    line = line.strip()
    line_num += 1
    new_line = line.translate(None, string.punctuation)
    words = new_line.split()
    for word in words:
        print "%s\t%s" % (word, 1)
