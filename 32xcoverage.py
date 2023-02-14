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

genomesize = int(sys.argv[1])
readnumber = int(sys.argv[2])
readlength = int(sys.argv[3])

reads = []
for i in range(readnumber):
	start = random.randint(0, genomesize - readlength)
	reads.append((start, start + readlength))

coverage = [0] * genomesize
for read in reads:
	for i in range(read[0], read[1]):
		coverage[i] += 1

mincoverage = coverage[0]
maxcoverage = coverage[0]
sumcoverage = 0

for i in range(genomesize):
	if coverage[i] < mincoverage:
		mincoverage = coverage[i]
	elif coverage[i] > maxcoverage:
		maxcoverage = coverage[i]
	sumcoverage += coverage[i]
avgcoverage = sumcoverage / genomesize
print(mincoverage, maxcoverage,'{:.4}'.format(avgcoverage))
"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
