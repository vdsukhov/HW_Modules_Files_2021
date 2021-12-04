mass_table = {"A" : 71.03711, "C" : 103.00919, "D" : 115.02694, "E" : 129.04259, "F" : 147.06841, "G" : 57.02146, "H" : 137.05891, "I" : 113.08406, "K" : 128.09496, "L" : 113.08406, "M" : 131.04049, "N" : 114.04293,"P" : 97.05276, "Q" : 128.05858, "R" : 156.10111, "S" : 87.03203,"T" : 101.04768, "V" : 99.06841, "W" : 186.07931, "Y" : 163.06333}

dna_codon = {'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y','TGC':'C', 'TGT':'C','TGG':'W'}

def parse(path_to_csv_file):
    list = []
    dict = {}
    with open(path_to_csv_file) as f:
        for line in f:
            line = line.strip('\n').strip('>')
            list.append(line)
            for i in range(0, len(list) - 1, 2):
              dict[list[i]] = list[i+1]
    return dict
def translate(dna_seq):
    protein = ''
    for i in range(len(dna_seq) - 2):
        seq = '' + dna_seq[i] + dna_seq[i + 1] + dna_seq[i + 2]
        if seq == 'ATG':
            for j in range(i + 3, len(dna_seq) - 2, 3):
                seq = '' + dna_seq[j] + dna_seq[j + 1] + dna_seq[j + 2]
                if seq in ['TAA', 'TAG', 'TGA']:
                    break
                else:
                    protein += dna_codon[seq]
            break
        else:
            continue
    return protein
def calc_mass(prot_seq):
    res = []
    for i in prot_seq:
        if i in mass_table:
            res.append(mass_table[i])
    return sum(res)
def orf(dna_seq):
    result = []
    compliment = {'A': 'T', 'C':'G', 'T':'A', 'G':'C'}
    rev_dna = ''
    for i in dna_seq[::-1]:
        rev_dna += compliment[i]
    def orf_prot(dna_seq):
        start = -1
        while start < len(dna_seq) - 2:
            protein = ''
            seq = '' + dna_seq[start] + dna_seq[start + 1] + dna_seq[start+ 2]
            start += 1
            if seq == "ATG":
                protein += dna_codon[seq]
                start += 2
                for i in range(start, len(dna_seq) - 2, 3):
                    seq = '' + dna_seq[i] + dna_seq[i + 1] + dna_seq[i + 2]
                    if seq in ['TAA', 'TAG', 'TGA']:
                        result.append(protein)
                        protein = ''
                        break
                    else:
                        protein += dna_codon[seq]
            else:
                continue
        return result
    res_orf = orf_prot(dna_seq)
    res_orf.extend(orf_prot(rev_dna))
    res_orf = list(set(res_orf))
    return res_orf