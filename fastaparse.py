
def parse(infile):
    scafs = {}
    descr = {}

    last = "no such scaff"
    newseq = ""
    with open(infile) as file:
        for line in file:
            if line[0] == ">":
                scafs[last] = newseq
                if " " in line:
                    last, line = line[1:].split(" ", 1)
                    descr[last] = line.strip()
                else:
                    last = line[1:].strip()
                    descr[last] = ""
                newseq = ""
            else:
                newseq += line.strip()
        scafs[last] = newseq
        del scafs["no such scaff"]
    return scafs


def translate(seq):
    seq = seq.upper()
    if "T" in seq:
        seq = seq.replace("T", "U")
    if "AUG" in seq:
        code = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L", "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L", "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M", "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V", "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S", "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P", "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T", "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A", "UAU":"Y", "UAC":"Y", "UAA":"0", "UAG":"0", "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q", "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K", "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E", "UGU":"C", "UGC":"C", "UGA":"0", "UGG":"W", "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R", "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R", "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}
        prot = "".join([code[seq[i:i+3]] for i in range(seq.find("AUG"), len(seq)-2, 3)])
        if "0" in prot:
            return prot.split("0")[0]
        else:
            return "no end"
    else:
        return "no start"


def calc_mass(s):
    return sum([{"G":57.021464,"A":71.037114, "S":87.032028, "P":97.052764, "V":99.068414, "T":101.047678, "C":103.009184, "I":113.084064, "L":113.084064, "N":114.042927, "D":115.026943, "Q":128.058578, "K":128.094963, "E":129.0422593, "M":131.040485, "H":137.058912, "F":147.068414, "R":156.101111, "Y":163.063329, "W":186.079313 }[i] for i in s])


def orf(seq, directions = "uni"):
    seq = seq.upper()
    prots = []
    prot = 0
    def wrap():
        st = seq.find("ATG")
        cur = -1
        while st != -1:
            cur += st+1
            prot = translate(seq[cur:])
            if prot != "no end":
                prots.append(prot)
            st = seq[cur+1:].find("ATG")
    wrap()
    seq = seq[::-1].replace("A", "1")
    seq = seq.replace("G", "2")
    seq = seq.replace("T", "A")
    seq = seq.replace("C", "G")
    seq = seq.replace("1", "T")
    seq = seq.replace("2", "C")
    wrap()
    return list(set(prots))



