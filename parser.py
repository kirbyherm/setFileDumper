### NOT SURE OF FUNCTIONALITY 
# would require 2 additional files:
#   1) list of ddas parameters
#   2) type of params as vals or bits
# K. Hermansen, 2020
###

import numpy as np
import math
import sys

#inputno = int(sys.argv[1])

#Function that returns the index of the 
#bit if it is set, and None if it is not
def get_bit(byteval,idx):
	if ((byteval&(1<<idx))!=0):
		return idx
	else:
		return 
#Function that returns an array of all set bits
def return_bit(val,low, high):
	bitlist = ''
	for i in range(low,high):
		bit = get_bit(val, i)
		if bit != None:
			bitlist += str(bit) + '_'
	return bitlist

inp = open(sys.argv[1],'r')
params = []
paramvals = []
for line in inp:
	linesp = line.split()
	params.append(linesp[0].lower())
	paramvals.append(linesp[1])

def fill_params_list(paramname, inputlist, inputvallist, dtype):
	paramlist = []
	paramlistval = []
	for index,item in enumerate(inputlist):
		if paramname in item:
			paramlist.append(item)
			if dtype == 'bit':
				paramlistval.append(return_bit(int(inputvallist[index]),0,16))
			elif dtype == 'val':
				paramlistval.append(inputvallist[index])
	for i in range(0,len(paramlist)):
		print paramlist[i], paramlistval[i]

fill_params_list(sys.argv[2], params, paramvals, sys.argv[3])

#print params[0:10], paramvals[0:10]
#return_bit(inputno,0,17)
