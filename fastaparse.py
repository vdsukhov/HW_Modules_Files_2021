mass_table = {"A" : 71.03711, "C" : 103.00919, "D" : 115.02694, "E" : 129.04259, "F" : 147.06841, "G" : 57.02146, "H" : 137.05891, "I" : 113.08406, "K" : 128.09496, "L" : 113.08406, "M" : 131.04049, "N" : 114.04293,"P" : 97.05276, "Q" : 128.05858, "R" : 156.10111, "S" : 87.03203,"T" : 101.04768, "V" : 99.06841, "W" : 186.07931, "Y" : 163.06333}

dna_codon = {"TTT":"F", "TTC":"F", "TTA":"L", "TTG":"L", "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L", "ATT":"I", "ATC":"I", "ATA":"I", "ATG":"M", "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V", "UTU":"S", "TCC":"S", "TCA":"S", "TCG":"S", "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P", "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T", "GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A", "TAT":"Y", "TAC":"Y", "TAA":"0", "TAG":"0", "CAT":"H", "CAC":"H", "CAA":"Q", "CAG":"Q", "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K", "GAT":"D", "GAC":"D", "GAA":"E", "GAG":"E", "TGT":"C", "TGC":"C", "TGA":"0", "TGG":"W", "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R", "AGT":"S", "AGC":"S", "AGA":"R", "AGG":"R", "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G"}

def parse(path_to_csv_file):
    my_list = []
    my_dict = {}
    try:
        with open(path_to_csv_file, "r") as my_file:
            for line in my_file:
              my_list.append(line)
            for i in range(0,len(my_list)-1,2):
              my_dict[my_list[i]] = my_list[i+1]

    except EOFError:
        print("Error, such file doesn't exist")
    return my_dict


def translate(dna_seq):
    prot = ''
    for i in range(0, len(dna_seq)-2, 3):
      codon = '' + dna_seq[i] + dna_seq[i+1] + dna_seq[i+2]
      prot += dna_codon[codon]
    return prot

    def calc_mass(prot_seq):
    res = []
    for i in prot_seq:
        if i in mass_table:
            res.append(mass_table[i])
    return sum(res)

def orf(rna_seq):
    acids = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L", "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L", "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M", "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V", "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S", "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P", "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T", "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A", "UAU":"Y", "UAC":"Y", "UAA":"0", "UAG":"0", "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q", "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K", "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E", "UGU":"C", "UGC":"C", "UGA":"0", "UGG":"W", "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R", "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R", "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}
    prot = []
    seq = rna_seq[rna_seq.find("AUG")+3:]
    for i in range(len(seq)//3):
        codon = seq[i*3:i*3+3]
        if codon in ["UGA","UAG","UAA"]:
            break
        prot.append(acids[codon])
    return "".join(prot)