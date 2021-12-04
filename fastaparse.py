mass_table = {"G":57.021464,"A":71.037114,"S":87.032028,"P":97.052764,"V":99.068414,"T":101.047678,"C":103.009184,"I":113.084064,"L":113.084064,"N":114.042927,"D":115.026943,"Q":128.058578, "K":28.094963,"E":129.042593,"M":131.040485,"H":137.058912,"F":147.068414,"R":156.101111,"Y":163.063329,"W":186.079313}
dna_codon = {'ATA':'I','ATC':'I','ATT':'I','ATG':'M','ACA':'T','ACC':'T','ACG':'T','ACT':'T','AAC':'N','AAT':'N','AAA':'K','AAG':'K','AGC':'S','AGT':'S','AGA':'R','AGG':'R','CTA':'L','CTC':'L','CTG':'L','CTT':'L','CCA':'P','CCC':'P','CCG':'P','CCT':'P','CAC':'H','CAT':'H','CAA':'Q','CAG':'Q','CGA':'R','CGC':'R','CGG':'R','CGT':'R','GTA':'V','GTC':'V','GTG':'V','GTT':'V','GCA':'A','GCC':'A','GCG':'A','GCT':'A','GAC':'D','GAT':'D','GAA':'E','GAG':'E','GGA':'G','GGC':'G','GGG':'G','GGT':'G','TCA':'S','TCC':'S','TCG':'S','TCT':'S','TTC':'F','TTT':'F','TTA':'L','TTG':'L','TAC':'Y','TAT':'Y','TAA':'_','TAG':'_','TGC':'C','TGT':'C','TGA':'_','TGG':'W'}


def parse(path_to_file_fasta):
  keys = []
  seq = []
  with open (path_to_file_fasta, "r") as fasta_file:
    for line in fasta_file:
      line = line.strip()
      if line.find(">") != -1:
        keys.append(line[1:])
      else:
        seq.append(line)
  fasta_file.close()
  fasta_dic = dict(zip(keys,seq))
  return(fasta_dic)

def calc_mass(prot_seq):
  mass_of_seq = 0
  for i in range(0,len(prot_seq)):
    mass = mass_table[prot_seq[i]]
    mass_of_seq += mass
  return(mass_of_seq)

def translate(dna_seq):
  prot = ''
  for i in range(0, len(dna_seq)-2):
    if dna_seq[i] =="A":
      if dna_seq[i+1] == "T":
        if dna_seq[i+2] == "G":
          j = i
          break
    else:
      continue
  try:
    for i in range(j, len(dna_seq)-2, 3):
      codon = dna_seq[i] + dna_seq[i+1] + dna_seq[i+2]
      if dna_codon[codon] == '_':
        return prot
        break
      else:
        prot += dna_codon[codon]
    return prot
  except KeyError:
    return ("No such codon")


def orf(dna_seq):
  chains = []
  index = []
  for i in range(len(dna_seq)-2):
    codon = dna_seq[i] + dna_seq[i+1] + dna_seq[i+2]
    am_ac = dna_codon[codon]
    if am_ac == 'M':
      index.append(i)
  for elem in index:
    protein_chain = ''
    for j in range(elem, len(dna_seq)-2, 3):
      codon = dna_seq[j] + dna_seq[j+1] + dna_seq[j+2]
      am_ac = dna_codon[codon]
      if am_ac != '_':
        protein_chain += am_ac
      else:
        break
    chains.append(protein_chain)
  second_seq = []
  for p in range(len(dna_seq)):
    if dna_seq[p] == 'A':
      second_seq.append('T')
    elif dna_seq[p] == 'T':
      second_seq.append('A')
    elif dna_seq[p] == 'G':
      second_seq.append('C')
    if dna_seq[p] == 'C':
      second_seq.append('G')
  opposite_dir = ''
  opposite_dir = ''.join(reversed(second_seq))
  index = []
  for i in range(len(dna_seq)-2):
    codon = opposite_dir[i] + opposite_dir[i+1] + opposite_dir[i+2]
    am_ac = dna_codon[codon]
    if am_ac == 'M':
      index.append(i)
  for elem in index:
    protein_chain = ''
    for j in range(elem, len(dna_seq)-2, 3):
      codon = opposite_dir[j] + opposite_dir[j+1] + opposite_dir[j+2]
      am_ac = dna_codon[codon]
      if am_ac != '_':
        protein_chain += am_ac
      else:
        break
    chains.append(protein_chain)
  return list(set(chains))