import mycsv 
import fastaparse 

dna_seq = "ACAGGACGGCATTGCCACGTCACGC\
CGTTTTGCCAGAGACATCGATCGCG\
AAGCCGATTTCGATGAGTCCCGCAT\
GCCTAAGGCACAATAGAATGTAGCA\
TCCAGACACTGAGGTGCGTCTGGAA\
AAAGACACTCAGGGATAAAAATCAC\
AGTACCACACAGTGCCGCAGCTCCG\
AATGTCGAGGTTCATATAATCGGAC\
CTTCTCTCTCGAAAGCTGACCTTCG\
ACATGTAAAAGATAAATCCAGCAGA\
TGCATGTAACCAAGGTCGGACCAGA"

print("#### The monoisotopic mass table for amino acids ####\n")
print(fastaparse.mass_table)
print("\n")

print("#### DNA Codon Table ####\n")
print(fastaparse.dna_codon)
print("\n")

print("#### Testing parse function ####\n")
res_dict = fastaparse.parse("fasta_data.txt")
print(res_dict)
print("\n")

print("#### Testing translate function ####\n")
print("This function will be tested inside orfs function\n")

print("#### Testing calc_mass function ####\n")
print(fastaparse.calc_mass("GTYCWIF"))
print("\n")

print("#### Testing open reading frames ####\n")
print(fastaparse.orfs(dna_seq))


