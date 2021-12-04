import os.path as path
mass_table = {'G': 57.021464, 'A': 71.037114, 'S': 87.032028, 'P': 97.052764, 'V': 99.068414, 'T': 101.047678,
              'C': 103.009184, 'I': 113.084064, 'L': 113.084064, 'N': 114.042927, 'D': 115.026943, 'Q': 128.058578,
              'K': 128.094963, 'E': 129.042593, 'M': 131.040485, 'H': 137.058912, 'F': 147.068414, 'R': 156.101111,
              'Y': 163.063329, 'W': 186.079313}

prot_dict = {'A': ['GCT', 'GCC', 'GCA', 'GCG'], 'R': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], 'N': ['AAT', 'AAC'],
             'D': ['GAT', 'GAC'], 'C': ['TGT', 'TGC'], 'Q': ['CAA', 'CAG'], 'E': ['GAA', 'GAG'],
             'G': ['GGT', 'GGC', 'GGA', 'GGG'], 'H': ['CAT', 'CAC'], 'I': ['ATT', 'ATC', 'ATA'],
             'L': ['CTT', 'CTC', 'CTA', 'CTG', 'TTA', 'TTG'], 'K': ['AAA', 'AAG'], 'M': ['ATG'], 'F': ['TTT', 'TTC'],
             'P': ['CCT', 'CCC', 'CCA', 'CCG'], 'S': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
             'T': ['ACT', 'ACC', 'ACA', 'ACG'], 'W': ['TGG'], 'Y': ['TAT', 'TAC'], 'V': ['GTT', 'GTC', 'GTA', 'GTG']}
dna_codon = {}
for key, value in prot_dict.items():
    for i in value:
        dna_codon[i] = key


def parse(file_path):
    abs_path = path.abspath(file_path)
    with open(abs_path) as f:
        seq_lines = [line.strip() for line in f]
    seq_dict = {}
    count = 0
    while count < len(seq_lines):
        seq_id = ""
        cur_seq = ""
        if seq_lines[count][0] == ">":
            seq_id = seq_lines[count][1:]
            count += 1
            while True:
                try:
                    if seq_lines[count][0] != ">":
                        cur_seq += seq_lines[count]
                        count += 1
                    else:
                        break
                except IndexError:
                    break
        seq_dict[seq_id] = cur_seq
    return seq_dict


def translate(dna_seq):
    protein = str()
    for i in range(len(dna_seq)-2):
        codon = dna_seq[i] + dna_seq[i+1] + dna_seq[i+2]
        if codon == "ATG":
            protein += dna_codon[codon]
            for j in range(i+3, len(dna_seq)-2, 3):
                codon = dna_seq[j] + dna_seq[j+1] + dna_seq[j+2]
                if codon == 'TAA' or codon == 'TGA' or codon == 'TAG':
                    break
                else:
                    protein += dna_codon[codon]
            break
        else:
            continue
    return protein


def calc_mass(prot_seq):
    mass = 0
    for ch in prot_seq:
        mass += mass_table[ch]
    return mass


def orf(dna_seq):
    compl_dna_seq = str()
    for i in range(len(dna_seq)):
        if dna_seq[i] == "A":
            compl_dna_seq += "T"
        elif dna_seq[i] == "T":
            compl_dna_seq += "A"
        elif dna_seq[i] == "G":
            compl_dna_seq += "C"
        else:
            compl_dna_seq += "G"
    rev_compl_dna_seq = compl_dna_seq[::-1]

    def getprot(dna_seq):
        protein_list = []
        count = 0
        while count < len(dna_seq) - 2:
            protein = ""
            codon = dna_seq[count] + dna_seq[count + 1] + dna_seq[count + 2]
            count += 1
            if codon == "ATG":
                protein += dna_codon[codon]
                count += 2
                for i in range(count, len(dna_seq) - 2, 3):
                    codon = dna_seq[i] + dna_seq[i + 1] + dna_seq[i + 2]
                    if codon == 'TAA' or codon == 'TGA' or codon == 'TAG':
                        protein_list.append(protein)
                        protein = ""
                        break
                    else:
                        protein += dna_codon[codon]
            else:
                continue
        return protein_list
    res_prot_list = getprot(dna_seq)
    res_prot_list.extend(getprot(rev_compl_dna_seq))
    res_prot_list = set(res_prot_list)
    res_prot_list = list(res_prot_list)
    return res_prot_list


