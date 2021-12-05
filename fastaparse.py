mass_table = {'G':'57.021464',
'A':'71.037114',
'S':'87.032028',
'P':'97.052764',
'V':'99.068414',
'T':'101.047678',
'C':'103.009184',
'I':'113.084064',
'L':'113.084064',
'N':'114.042927',
'D':'115.026943',
'Q':'128.058578',
'K':'128.094963',
'E':'129.042593',
'M':'131.040485',
'H':'137.058912',
'F':'147.068414',
'R':'156.101111',
'Y':'163.063329',
'W':'186.079313'}

dna_codon={'I':['ATT','ATC','ATA'], 'L':['CTT', 'CTC', 'CTA', 'CTG', 'TTA', 'TTG'], 'V':['GTT', 'GTC', 'GTA', 'GTG'], 'F':['TTT', 'TTC'], 'M':['ATG'], 'C':['TGT', 'TGC'], 'A':['GCT', 'GCC', 'GCA', 'GCG'], 'G':['GGT', 'GGC', 'GGA', 'GGG'], 'P':['CCT', 'CCC', 'CCA', 'CCG'], 'T':['ACT', 'ACC', 'ACA', 'ACG'], 'S':['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'], 'Y':['TAT','TAC'], 'W':['TGG'], 'Q':['CAA', 'CAG'], 'N':['AAT', 'AAC'], 'H':['CAT', 'CAC'], 'E':['GAA', 'GAG'], 'D':['GAT', 'GAC'], 'K':['AAA', 'AAG'], 'R':['CGT','CGC', 'CGA', 'CGG', 'AGA', 'AGG']}

def parse(file_path):
    dictr ={}
    seq_id = []
    seq = []
    sequence = ''
    with open(file_path) as inf:
        for line in inf:
            if line.startswith('>'):
                seq_id.append(line.strip().strip('>'))
                seq.append(sequence)
                sequence = ''
            else:
                sequence +=line.strip()
        seq.append(sequence)
        del seq[0]
        for i in range(len(seq_id)):
            dictr[seq_id[i]]=seq[i]
        return dictr
        


def calc_mass(prot_seq):
    counter = 0
    for i in prot_seq:
        counter+=float(mass_table[i])
    return counter

def translate(dna_seq):
    peptide = ''
    a = dna_seq.find('ATG')
    while a<=len(dna_seq):
        if dna_seq[a:a+3] == 'TAA' or dna_seq[a:a+3] == 'TAG' or dna_seq[a:a+3] == 'TGA':
            break
        else:
            for acid, codon in dna_codon.items():
                if dna_seq[a:a+3] in codon:
                    peptide +=acid
                    break
            a+=3
    return peptide
dna_seq = "ACAGGACGGCATTGCCACGTCACGCCGTTTTGCCAGAGACATCGATCGCGAAGCCGATTTCGATGAGTCCCGCATGCCTAAGGCACAATAGAATGTAGCATCCAGACACTGAGGTGCGTCTGGAAAAAGACACTCAGGGATAAAAATCACAGTACCACACAGTGCCGCAGCTCCGAATGTCGAGGTTCATATAATCGGACCTTCTCTCTCGAAAGCTGACCTTCGACATGTAAAAGATAAATCCAGCAGATGCATGTAACCAAGGTCGGACCAGA"





def orf(dna_seq):
    orfs =[]
    d =dna_seq.find('ATG')
    print(d)
    for i in range(3):
        starts = []
        while i <= len(dna_seq):
            if translate(dna_seq[i:i+3])=='M':
                    starts.append(i)
            i+=3
        print(starts)
        for j in starts:
            orfs.append(translate(dna_seq[j:]))
    return set(orfs)


print(orf(dna_seq))
