# 32xcoverage.py

# Write a program that simulates a shotgun resequencing project
# How uniformly do the reads "pile up" on a chromosome?
# How much of that depends on sequencing depth?

# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line

# Hint: make the problem smaller, so it's easier to visualize and debug
# Hint: if you don't understand the context of the problem, ask for help
# Hint: if you are undersampling the ends, do something about it

# Note: you will not get exactly the same results as the command line below
import random
import sys

gsize = int(sys.argv[1])
rnumber = int(sys.argv[2])
rlength = int(sys.argv[3])

reads = []
for i in range(rnumber):
	beginning = random.randint(0, gsize - rlength)
	reads.append((beginning, beginning + rlength))

coverage = [0] * gsize
for read in reads:
	for i in range(read[0], read[1]):
		coverage[i] += 1

minC = coverage[0]
maxC = coverage[0]
sumC = 0
for i in range(gsize):
	if coverage[i] < minC:
		minC = coverage[i]
	elif coverage[i] > maxC:
		maxC = coverage[i]
	sumC += coverage[i]
avgC = sumC / gsize
print(minC, maxC,'{:.4}'.format(avgC))
"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
