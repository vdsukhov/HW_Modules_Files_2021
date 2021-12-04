mass_table = {"G":57.021464 ,
              "A":71.037114 ,
              "S":87.032028 ,
              "P":97.052764 ,
              "V":99.068414 ,
              "T":101.047678 ,
              "C":103.009184 ,
              "I":113.084064 ,
              "L":113.084064 ,
              "N":114.042927 ,
              "D":115.026943 ,
              "Q":128.058578 ,
              "K":128.094963 ,
              "E":129.042593 ,
              "M":129.042593 ,
              "H":137.058912 ,
              "F":147.068414 ,
              "R":156.101111 ,
              "Y":163.063329 ,
              "W":186.079313 ,
                    }

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
    """
    parses a fasta file and returns a dictionary. The dictionary
    consists of pairs seq_id as string and the sequence itself seq as string or list .
    """
    res = {}
    try:
        with open(file_path, "r") as f:
            line_f = f.readlines()
    except FileNotFoundError:
        print("Error, such file doesn't exist")
        return {}
    
    for line in line_f:
        if line[0]==">":
            id=line[1:].replace("\n", "")
            res[id]=""
        else:
            res[id]=res[id]+line.replace("\n", "")
    return res

def translate(dna_seq):
    """
    This function takes DNA sequence as a string and returns the
    protein string encoded by dna_seq as a string.
    """
    ret=""
    for i in range(0, (len(dna_seq)//3)*3, 3):
        ret+=dna_codon[dna_seq[i:i+3]]
    return ret

def calc_mass(prot_seq):
    """
    This function takes a string encoding a protein and returns the
    mass as float .
    """
    ret=0
    
    for prot in prot_seq:
        ret+=mass_table[prot]
    return ret

def opposite_dna(dna_seq):
    tmp=""
    
    for c in dna_seq:
        if c=="A":
            tmp+="T"
        elif c=="C":
            tmp+="G"
        elif c=="G":
            tmp+="C"
        elif c=="T":
            tmp+="A"
        else:
            print("---ERROR BAD CHAR IN THE DNA---")
            return None
    
    return tmp[::-1]

def orf(dna_seq):
    """
    This function takes DNA sequence as string and returns list of every
    distinct candidate protein string that can be translated from Open Reading Frames of dna_seq .
    """
    
    dna_seq_cpy=dna_seq.replace(" ", "")
    ret =[]
    dna_list=[dna_seq_cpy, opposite_dna(dna_seq_cpy)]
    
    for dna in dna_list:
        idx = dna.find("ATG")
        while idx>-1:
            tr = translate(dna[idx:])
            stop_idx = tr.find("STOP")
            if stop_idx>-1:
                seq = tr[:stop_idx]
                ret.append(seq)
            dna = dna[idx+3:]
            idx = dna.find("ATG")
        
    return list(set(ret))