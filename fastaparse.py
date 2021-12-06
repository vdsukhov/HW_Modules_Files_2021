mass_table = {'G':57.021464, 'A':71.037114 , 
               'S':87.032028 , 'P':97.052764 ,
               'V':99.068414 ,
              'T':101.047678 , 'C':103.009184 ,
              'I':113.084064 , 'L':113.084064 ,
               'N':114.042927 , 
              'D':115.026943 , 'Q':128.058578 ,
               'K':128.094963 , 'E':129.042593 ,
               'M':131.040485 ,
              'H':137.058912 , 'F':147.068414 , 
               'R':156.101111 , 'Y':163.063329 ,
               'W':186.079313}
dna_codon = {'TTT':'F' , 'TTC':'F' , 'TTA':'L' , 'TTG':'L' ,
         'TCT':'S' , 'TCC':'S' ,
        'TCA':'S' , 'TCG':'S' , 'TAT':'Y' , 'TAC':'Y' ,
         'TGT':'C' , 'TGC':'C' ,
        'TGG':'W' , 'CTT':'L' , 'CTC':'L' , 'CTA':'L' ,'CTG':'L' ,
         'CCT':'P' ,
        'CCC':'P' , 'CCA':'P' , 'CCG':'P' , 'CAT':'H' , 'CAC':'H' ,
         'CAA':'Q' ,
        'CAG':'Q' ,'CGT':'R' ,'CGC':'R' ,'CGA':'R' ,'CGG':'R' ,
         'ATT':'I' ,
        'ATC':'I' ,'ATA':'I' ,'ACT':'T' ,'ACC':'T', 'ACA':'T' ,
        'ACG':'T' , 'AAT':'N' ,'AAC':'N' ,'AAA':'K' ,'AAG':'K' ,
         'ATG':'M', 'AGT':'S' ,
        'AGC':'S' ,'AGA':'R' ,'AGG':'R' , 'GTT':'V' , 'GTC':'V' ,
         'GTA':'V' ,'GTG':'V' ,
        'GCT':'A' ,'GCC':'A' ,'GCA':'A' , 'GCG':'A' ,
         'GAT':'D' ,'GAC':'D' ,'GAA':'E' ,
        'GAG':'E' ,'GGT':'G' ,'GGC':'G' ,'GGA':'G' ,'GGG':'G' }


def parse(file_path):
    dic = {}
    fasta_list = []
    with open(file_path) as f:
        for line in f:
            current_string = line.strip()
            fasta_list.append(current_string)
        for i in range(len(fasta_list)):
            value = str()
            if fasta_list[i][0] == ">":
                key = fasta_list[i]
                for j in range(i+1, len(fasta_list)):
                    if fasta_list[j][0] != ">":
                        value += fasta_list[j]
                    elif fasta_list[j][0] == ">":
                        break
                key =key.replace(">", "")
                dic[key] = value
        print(dic)

def translate(dna_seq):
    s = []
    with open(dna_seq) as inp_f:
        for line in inp_f:
            line = line.strip()
            line = line.replace("\\", "")
            s.append(line)
        res = ''.join([el for el in s])

    dna_seq = res
    n=3
    cod = []
    cod_r = []
    start = "ATG"
    stop = ("TAA", "TAG", "TGA")
    prot = []
    st = dna_seq.index(start)
    cod = dna_seq[st+3:]               
    cod = [cod[i:i+3] for i in range (0, len(cod), 3)]            
   # Protein coded sequence        
    for i in cod:       
        if i not in stop:
            cod_r.append(i)
        else:
            break    
    # Replace codons by amino acides
    for el in cod_r:
        prot.append(dna_codon.get(el, ''))      
    prot = ''.join(prot)  
    print(prot)

def calc_mass(prot):
    s = []
    with open(prot) as inp_f:
        for line in inp_f:
            line = line.strip()
            line = line.replace("\\", "")
            line = line.replace("prot =", "")
            line = line.replace('"', '')
            line = line.strip()
            s.append(line)
        res = ''.join([el for el in s])

    prot = res
    mass = []
    for el in prot:
        mass.append(mass_table.get(el, ''))  
    w=sum(mass)
    print(w)
