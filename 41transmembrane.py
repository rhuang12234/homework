# 41transmembrane.py

# Write a program that predicts which proteins in a proteome are transmembrane

# Transmembrane proteins are characterized by having
#    1. a hydrophobic signal peptide near the N-terminus
#    2. other hydrophobic regions to cross the plasma membrane

# Both the signal peptide and the transmembrane domains are alpha-helices
# Therefore, they do not contain Proline

# Hydrophobicity can be measured by Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot

# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa

# Hint: copy mcb185.py to your homework repo and import that
# Hint: create a function for KD calculation
# Hint: create a function for hydrophobic alpha-helix
# Hint: use the same function for both signal peptide and transmembrane
import sys
import gzip
import mcb185

def hydropathy(seq):
	total = 0
	for DNA in seq:
		if DNA == 'A':
			total += 1.8
		elif DNA == 'C':
			total += 2.5
		elif DNA == 'D':
			total += -3.5
		elif DNA == 'E':
			total += -3.5
		elif DNA == 'F':
			total += 2.8
		elif DNA == 'G':
			total += -0.4
		elif DNA == 'H':
			total += -3.2
		elif DNA == 'I':
			total += 4.5
		elif DNA == 'K':
			total += -3.9
		elif DNA == 'L':
			total += 3.8
		elif DNA == 'M':
			total += 1.9
		elif DNA == 'N':
			total += -3.5
		elif DNA == 'P':
			total += -1.6
		elif DNA == 'Q':
			total += -3.5
		elif DNA == 'R':
			total += -4.5
		elif DNA == 'S':
			total += -0.8
		elif DNA == 'T':
			total += -0.7
		elif DNA == 'V':
			total += 4.2
		elif DNA == 'W':
			total += -0.9
		elif DNA == 'Y':
			total += -1.3 
		
	return total/len(seq)

def is_transmembrane(sequence):
	signal_peptide = sequence[:30]
	hydrophobic_region = sequence[30:41]
	signal_kd = hydropathy(signal_peptide)
	hydrophobic_kd = hydropathy(signal_peptide)
	return signal_kd > 2.5 and hydrophobic_kd > 2.0

with gzip.open(sys.argv[1], 'rt') as fp:
	header = ''
	sequence = ''
	for line in fp:
		line = line.strip()
		if line.startswith('>'):
			if header and is_transmembrane(sequence):
				print(header)
			header = line[1:]
			sequence = ''
		else:
			sequence += line
		
"""
python3 41transmembrane.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_protein.faa.gz
NP_414560.1 Na(+):H(+) antiporter NhaA [Escherichia coli str. K-12 substr. MG1655]
NP_414568.1 lipoprotein signal peptidase [Escherichia coli str. K-12 substr. MG1655]
NP_414582.1 L-carnitine:gamma-butyrobetaine antiporter [Escherichia coli str. K-12 substr. MG1655]
NP_414607.1 DedA family protein YabI [Escherichia coli str. K-12 substr. MG1655]
NP_414609.1 thiamine ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414653.1 protein AmpE [Escherichia coli str. K-12 substr. MG1655]
NP_414666.1 quinoprotein glucose dehydrogenase [Escherichia coli str. K-12 substr. MG1655]
NP_414695.1 iron(III) hydroxamate ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414699.1 PF03458 family protein YadS [Escherichia coli str. K-12 substr. MG1655]
NP_414717.2 CDP-diglyceride synthetase [Escherichia coli str. K-12 substr. MG1655]
...
"""
