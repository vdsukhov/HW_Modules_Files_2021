mass_table = {
    "G": 57.021464,
    "A": 71.037114,
    "S": 87.032028,
    "P": 97.052764,
    "V": 99.068414,
    "T": 101.047678,
    "C": 103.009184,
    "I": 113.084064,
    "L": 113.084064,
    "N": 114.042927,
    "D": 115.026943,
    "Q": 128.058578,
    "K": 128.094963,
    "E": 129.042593,
    "M": 131.040485,
    "H": 137.058912,
    "F": 147.068414,
    "R": 156.101111,
    "Y": 163.063329,
    "W": 186.079313,
}

dna_codon = {'TTT': 'F',     'TCT': 'S',      'TAT': 'Y',      'TGT': 'C',
    'TTC': 'F',     'TCC': 'S',      'TAC': 'Y',      'TGC': 'C',
    'TTA': 'L',     'TCA': 'S',      'TAA': 'stop',      'TGA': 'stop',
    'TTG': 'L',     'TCG': 'S',      'TAG': 'stop',      'TGG': 'W',
    'CTT': 'L',     'CCT': 'P',      'CAT': 'H',      'CGT': 'R',
    'CTC': 'L',     'CCC': 'P',      'CAC': 'H',      'CGC': 'R',
    'CTA': 'L',     'CCA': 'P',      'CAA': 'Q',      'CGA': 'R',
    'CTG': 'L',     'CCG': 'P',      'CAG': 'Q',      'CGG': 'R',
    'ATT': 'I',     'ACT': 'T',      'AAT': 'N',      'AGT': 'S',
    'ATC': 'I',     'ACC': 'T',      'AAC': 'N',      'AGC': 'S',
    'ATA': 'I',     'ACA': 'T',      'AAA': 'K',      'AGA': 'R',
    'ATG': 'M',     'ACG': 'T',      'AAG': 'K',      'AGG': 'R',
    'GTT': 'V',     'GCT': 'A',      'GAT': 'D',      'GGT': 'G',
    'GTC': 'V',     'GCC': 'A',      'GAC': 'D',      'GGC': 'G',
    'GTA': 'V',     'GCA': 'A',      'GAA': 'E',      'GGA': 'G',
    'GTG': 'V',     'GCG': 'A',      'GAG': 'E',      'GGG': 'G'}

def parse(file_path):
    seq_id = ''
    all_seq_id = []
    seq = ''
    all_seq = []
    with open(file_path) as inp_f:
        for line in inp_f:
            line = line.strip()
            if line[0] == '>':
                if seq_id:
                    all_seq_id.append(seq_id)
                    all_seq.append(seq)
                seq_id = line[1:]
            elif line:
                seq += line
        all_seq_id.append(seq_id)
        all_seq.append(seq)
    seq_dict = dict()
    for i in range(len(all_seq_id)):
        seq_dict[all_seq_id[i]] = all_seq[i]
    return seq_dict

def translate(dna_seq):
    ind = dna_seq.find('ATG') + 3
    protein = ''
    while dna_seq[ind:ind + 3] not in ['TAA', 'TAG', 'TGA'] and ind < len(dna_seq) - 2:
        protein += dna_codon[dna_seq[ind:ind + 3]]
        ind += 3
    return protein

def calc_mass(prot_seq):
    mass = 0
    for i in prot_seq:
        mass += mass_table[i]
    return mass

def orf(dna_seq):
    orfs = []
    compl = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    dna_seq_rev = ''
    for i in reversed(dna_seq):
        dna_seq_rev += compl[i]
    for seq in (dna_seq, dna_seq_rev):
        for k in range(3):
            codons = [seq[i:i + 3] for i in range(k, len(seq), 3)]
            start = -1
            while True:
                try:
                    start = codons.index('ATG', start + 1)
                except ValueError:
                    break
                codons = codons[start:]
                protein = ''
                for codon in codons:
                    if codon in ['TAA', 'TAG', 'TGA']:
                        break
                    if len(codon) != 3:
                        continue
                    protein += dna_codon[codon]
                else:
                    protein = ''
                if protein:
                    orfs.append(protein)
    return orfs
