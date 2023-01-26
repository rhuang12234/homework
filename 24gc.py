# 24gc.py

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'
GCamount = 0
for base in dna:
	if base  == 'G' or base == 'C':
		GCamount += 1
GCPercent = (GCamount / len(dna))
print('{:.2f}'.format(GCPercent))
"""
python3 24gc.py
0.42
"""
