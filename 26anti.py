# 26anti.py

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

# Variation: try this with the range() function and slice syntax

dna = 'ACTGAAAAAAAAAAA'
ReverseComplement = ""
for DNA in dna[::-1]:
	if DNA == "A":
		ReverseComplement += "T"
	elif DNA == "C":
		ReverseComplement += "G"
	elif DNA == "G":
		ReverseComplement += "C"
	elif DNA == "T":
		ReverseComplement += "A"
print(ReverseComplement)
"""
python3 26anti.py
TTTTTTTTTTTCAGT
"""
