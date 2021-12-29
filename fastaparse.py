mass_table = {
'A': 71.03711, 'G': 57.02146, 'M': 131.04049, 'S': 87.03203,
'C': 103.00919, 'H': 137.05891, 'N': 114.04293, 'T': 101.04768,
'D': 115.02694, 'I': 113.08406, 'P': 97.05276, 'V': 99.06841,
'E': 129.04259, 'K': 128.09496, 'Q': 128.05858, 'W': 186.07931,
'F': 147.06841, 'L': 113.08406, 'R': 156.10111, 'Y': 163.06333
}

dna_codon = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
}

def parse(file_path):
    seq_id = []
    seq = []
    with open(file_path) as fasta:
        for line in fasta:
            line = line.strip()
            if line[0] == ">":
                seq_id.append(line[1:])
                print
            else:
                seq.append(line)
    fasta.close()
    fasta_dictionary = {}
    for i in range(len(seq_id)):
        fasta_dictionary[seq_id[i]] = seq[i]
    return fasta_dictionary


def translate(dna_seq):
    prot_seq_list = []
    try:
        for i in range (0, len(dna_seq) - 2):
            if dna_seq[i] == "A" and dna_seq[i+1] == "T" and dna_seq[i+2] == "G":
                start = i
        for i in range(start, len(dna_seq) - 2, 3):
            codon = dna_seq[i] + dna_seq[i + 1] + dna_seq[i + 2]
            amino_a = dna_codon[codon]
            prot_seq_list.append(amino_a)

        for i in range(len(prot_seq_list)):
            if prot_seq_list[i] == '_':
                prot_seq_list_cut = prot_seq_list[:i]

        prot_seq = ''.join(prot_seq_list_cut)
        return prot_seq
    except UnboundLocalError:
        return "No start or stop codon"

def calc_mass(prot_seq):
    mass_total = 0
    for i in range(0,len(prot_seq)):
        mass = mass_table[prot_seq[i]]
        mass_total += mass
    return mass_total

def orf(dna_seq):
    seq_total = []
    index = []
    for i in range(len(dna_seq)-2):
        codon = dna_seq[i] + dna_seq[i+1] + dna_seq[i+2]
        if codon == 'ATG':
            index.append(i)
            amino_a = dna_codon[codon] 
    for elem in index:
        protein_list = []
        for j in range(elem, len(dna_seq)-2, 3):
            codon = dna_seq[j] + dna_seq[j+1] + dna_seq[j+2]
            amino_a = dna_codon[codon]
            if amino_a != '_':
                protein_list.append(amino_a)
            else:
                break
        protein_seq = ''.join(protein_list)
        seq_total.append(protein_seq)
    another_seq = []
    for p in range(len(dna_seq)):
        if dna_seq[p] == 'A':
            another_seq.append('T')
        elif dna_seq[p] == 'T':
            another_seq.append('A')
        elif dna_seq[p] == 'G':
            another_seq.append('C')
        if dna_seq[p] == 'C':
            another_seq.append('G')
    another_way = ''.join(reversed(another_seq))
    index = []
    for i in range(len(dna_seq)-2):
        codon = another_way[i] + another_way[i+1] + another_way[i+2]
        if codon == 'ATG':
            index.append(i)
            amino_a = dna_codon[codon] 
    for elem in index:
        protein_list = []
        for j in range(elem, len(dna_seq)-2, 3):
            codon = another_way[j] + another_way[j+1] + another_way[j+2]
            amino_a = dna_codon[codon]
            if amino_a != '_':
                protein_list.append(amino_a)
            else:
                break
        protein_seq = ''.join(protein_list)
        seq_total.append(protein_seq)
    return list(set(seq_total))
