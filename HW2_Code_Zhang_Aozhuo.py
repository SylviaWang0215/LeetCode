print'''\nSTSCI 4060 HW2'''
print'''Name: Aozhuo Zhang'''
print'''NetID: az386'''
print '\n*****Question1*****\n'

#develop powerball lottery game, select first five number from white ball group(1-59). Select sixth number from red group(1-35).

import random
import re
from random import randint



print '\n*****Question2*****\n'

numline = 0
numword = 0
numchar = 0
with open(r'/Users/mac/Documents/Code/LeetCode/AboutCornell.txt', 'r')as f:
    data = f.readlines()

blankline = data.count('\r\n')
numline = len(data) - blankline

blankspace = 0
for item in data:
    temp = item.split()
    #print temp

    str1 = ''.join(temp)

    numchar += len(str1)
    numword += len(temp)
    blankspace += len(temp)

str1 = ''.join(data)

print "In the article there are " + str(numline) +" lines, " + str(numword) + " words, " + str(numchar) \
      + " characters (excludint whitespaces) and " + str(blankline + 1) + " paragragps. "