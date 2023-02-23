# 42dust.py

# Write a program that performs entropy filtering on nucleotide fasta files
# Windows that are below the entropy threshold are replaced by N

# Program arguments include file, window size, and entropy threshold

# Output should be a fasta file with sequence wrapped at 60 characters

# Hint: use the mcb185 library
# Hint: make up some fake sequences for testing

# Note: don't worry about "centering" the entropy on the window (yet)
import mcb185
import sys
import gzip
import math

def entropy_calculation(seq):

	counts = [0, 0, 0, 0]

	for base in seq:
		if base == 'A':
			counts[0] += 1
		elif base == 'C':
			counts[1] += 1
		elif base == 'G':
			counts[2] += 1
		elif base == 'T':
			counts[3] += 1
	total = len(seq)
	entropy = 0
	for count in counts:
		if count > 0:
			frequency = count / total
			entropy += -frequency * math.log2(frequency)
	return entropy			

def filter_genome(genome, window_size, entropy_threshold):
	filtered_genome = ''
	for i in range(len(genome) - window_size):
		window = genome[i:i+window_size]
		entropy = entropy_calculation(window)
		if entropy >= entropy_threshold:
			filtered_genome += window
		else:
			filtered_genome += 'N' * window_size
	return filtered_genome
	
window_size = int(sys.argv[2])
entropy_threshold = float(sys.argv[3])

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	genome = seq[:60]
	filtered_genome = filter_genome(genome, window_size, entropy_threshold)
	print(filtered_genome)

"""
python3 42dust.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz 11 1.4
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGNTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTNNNNNNNAAAAAGAGTGTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGNNNNNNNNNNNATTTTATTGACTTAGG
TCACNNAATACTTTAACCAATATAGGCATAGCGCACAGNCNNNNAAAAATTACAGAGTNN
ACAACATCCATGAAACGCATTAGCACCACCATNNNNNNNACCATCACCATTACCACAGGT
AACNGTGCGGGCTGACGCGTACAGNNNNNNNNGAAAAAAGCCCGCACCTGACAGTGCNNN
NNNTTTTTTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
ANNCANGGGCAGGTGGCCANCGNNNNNNNTNNNCCCGNNNNNNNNNCCAACCACCTGGTG
GCGATNATTGNNAAAACCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA
...
"""
