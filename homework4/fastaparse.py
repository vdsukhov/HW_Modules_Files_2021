'''
- The monoisotopic mass table for amino acids as a dictionary mass_table
- DNA codon table as a dictionary dna_codon
- Function parse(file_path) that parses a fasta file and returns a dictionary. The dictionary consists of pairs seq_id as string and the sequence itself seq as string or list .
- Function translate(dna_seq) . This function takes DNA sequence as a string and returns the protein string encoded by dna_seq as a string.
- Function calc_mass(prot_seq) . This function takes a string encoding a protein and returns the mass as float.
- Function orf(dna_seq) . This function takes DNA sequence as string and returns list of every distinct candidate protein string that can be translated from Open Reading Frames of dna_seq .
''' 

import re

mass_table = {"A" : 71.03711, "C" : 103.00919, "D" : 115.02694, "E" : 129.04259,
                "F" : 147.06841, "G" : 57.02146, "H" : 137.05891, "I" : 113.08406,
                "K" : 128.09496, "L" : 113.08406, "M" : 131.04049, "N" : 114.04293,
                "P" : 97.05276, "Q" : 128.05858, "R" : 156.10111, "S" : 87.03203,
                "T" : 101.04768, "V" : 99.06841, "W" : 186.07931, "Y" : 163.06333}


dna_codon = {"TTT" : "F", "CTT" : "L", "ATT" : "I", "GTT" : "V",
           "TTC" : "F", "CTC" : "L", "ATC" : "I", "GTC" : "V",
           "TTA" : "L", "CTA" : "L", "ATA" : "I", "GTA" : "V",
           "TTG" : "L", "CTG" : "L", "ATG" : "M", "GTG" : "V",
           "TCT" : "S", "CCT" : "P", "ACT" : "T", "GCT" : "A",
           "TCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A",
           "TCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A",
           "TCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A",
           "TAT" : "Y", "CAT" : "H", "AAT" : "N", "GAT" : "D",
           "TAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D",
           "TAA" : "STOP", "CAA" : "Q", "AAA" : "K", "GAA" : "E",
           "TAG" : "STOP", "CAG" : "Q", "AAG" : "K", "GAG" : "E",
           "TGT" : "C", "CGT" : "R", "AGT" : "S", "GGT" : "G",
           "TGC" : "C", "CGC" : "R", "AGC" : "S", "GGC" : "G",
           "TGA" : "STOP", "CGA" : "R", "AGA" : "R", "GGA" : "G",
           "TGG" : "W", "CGG" : "R", "AGG" : "R", "GGG" : "G" 
           }

def parse(file_path): 
	result = dict()
	with open(file_path, 'r') as file_h:
		data = file_h.read()
		data_splitted_by_lines = data.split('\n') 
		for elem in data_splitted_by_lines: 
			if elem.startswith('>'):
				result[elem[1:]] = data_splitted_by_lines[data_splitted_by_lines.index(elem) + 1]
	return result

def translate(dna_seq): 
        protein_sequence = ""
        if len(dna_seq)%3 == 0:
                for i in range(0, len(dna_seq), 3):
                        codon = dna_seq[i:i + 3]
                        protein_sequence+= dna_codon[codon]
        return protein_sequence

def calc_mass(prot_seq): 
	weight = sum(mass_table[p] for p in prot_seq)
	return weight 

def revcomp(dna_seq):
    return dna_seq[::-1].translate(str.maketrans("ATGC","TACG"))

def orfs(dna):
        result = [] 
        pattern = re.compile(r'(?=(ATG(?:...)*?)(?=TAG|TGA|TAA))')
        matchings = set(pattern.findall(dna) + pattern.findall(revcomp(dna)))
        for elem in matchings:
                result.append(translate(elem)) 
        return result 

