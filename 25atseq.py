# 25atseq.py

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

# Note: set random.seed() if you want repeatable random numbers
import random

size = 30
percentAT = 0.6

dna =''
countAT = 0
for i in range(size):
	r = random.random()
	if r < percentAT / 2:
		dna += 'A'
		countAT += 1
	elif r < percentAT:
		dna += 'T'
		countAT += 1
	else:
		if random.random() < 0.5:
			dna += 'C'
		else:
			dna += 'G'
newpercentAT = countAT / size
print(len(dna))
print(newpercentAT)
print(dna)
"""
python3 25atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""

