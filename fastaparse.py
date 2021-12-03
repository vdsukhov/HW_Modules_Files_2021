mass_table = {'G':57.021464, 'A':71.037114, 'S':87.032028, 'P':97.052764, 'V':99.068414, 'T':101.047678, 'C':103.009184,'I':113.084064, 'L':113.084064, 'N':114.042927, 'D':115.026943, 'Q':128.058578, 'K':128.094963, 'E':129.042593, 'M':131.040485, 'H':137.058912, 'F':147.068414, 'R':156.101111, 'Y':163.063329, 'W':186.079313}

dna_codon = {'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R', 'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A','GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 'TAC':'Y', 'TAT':'Y', 'TGC':'C', 'TGT':'C', 'TGG':'W', 'TAA':'_', 'TAG':'_', 'TGA':'_'}

def parse(path):
  with open(path) as inp_f:
      headers = []
      seqs = []
      for line in inp_f:
        if line.startswith('>fasta_'):
          headers.append(line.strip())
        else:
          seqs.append(line.strip())
  dict1 = {}
  for i in range(len(headers)):
    dict1[headers[i]] = seqs[i]
  return dict1

def translate(dna_seq):
    prot = ''
    for i in range(0, len(dna_seq)-2, 3):
      codon = '' + dna_seq[i] + dna_seq[i+1] + dna_seq[i+2]
      prot += dna_codon[codon]
    return prot

def calc_mass(prot_seq):
  mass = 0
  for i in prot_seq:
      mass += mass_table[i]
  return mass

def reverse(dna_seq):
  rev_dna = ''
  for i in dna_seq[::-1]:
    if i == 'A':
      rev_dna += 'T'
    elif i == 'T':
      rev_dna += 'A'
    elif i == 'C':
      rev_dna += 'G'
    else:
      rev_dna += 'C'
  return rev_dna

def orf1(dna_seq, result):
  for i in range(len(dna_seq) - 2):
    if dna_seq[i:i + 3] == 'ATG':
      j = i
      prot = ''
      codon = 'ATG'
      while dna_codon[codon] != "_":
          prot += dna_codon[codon]
          j += 3
          if j > len(dna_seq) - 3:
              break
          codon = dna_seq[j:j + 3]
      if dna_codon[codon] == "_" and prot not in result:
        result.append(prot)
  return result

def orf(dna_seq):
  result = []
  orf1(dna_seq, result)
  orf1(reverse(dna_seq), result)
  return result