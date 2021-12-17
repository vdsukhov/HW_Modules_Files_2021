class Reader:
    def __init__(self, name):
        self.file = open(name)
        print()

    def read (self):
        line = self.file.readline()
        if not line:
            return None
        return line.upper()

    def __del__ (self):
        self.file.close()
        print()

class Lexer:
    def __init__(self, reader):
        self.reader = reader
        self.line = None
        self.index = 0

    def next(self):
        char = self.__next_char()
        if char == None:
            return None
        if char == ">":
            header = ""
            while char != None and char != "\n":
                header = header + char
                char = self.__next_char()
            return header
        else:
            seq = ""
            while char != None and char != ">":
                if char != "\n":
                    if char not in "ATCGN":
                        raise Exception("This is not a nucleotidic sequence")
                    seq = seq + char
                char = self.__next_char()
            self.index = self.index - 1
            return seq

    def __next_char(self):
        if self.line == None or self.index >= len(self.line):
            self.line = self.reader.read()
            self.index = 0
        if self.line == None:
            return None

        char = self.line[self.index]
        self.index = self.index + 1
        return char



class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
    def parse_all(self):
        dict = {}
        while True:
            key = self.lexer.next()
            if key and key[0] == ">":
                value = self.lexer.next()
                if value and value[0] != ">":
                    dict[key[1:]] = value
                else:
                    raise Exception("Empty sequence")
            else:
                if not key:
                    return dict
                raise Exception("Invalid key")

def parse(file_path):
    myReader = Reader(file_path)
    myLexer = Lexer(myReader)
    myParser = Parser(myLexer)
    return myParser.parse_all()


mass_table = {
    "A": 71.03711,
    "R": 156.10111,
    "N": 114.04293,
    "D": 115.02694,
    "C": 103.00919,
    "E": 129.04259,
    "Q": 128.05858,
    "G": 57.02146,
    "H": 137.05891,
    "I": 113.08406,
    "L": 113.08406,
    "K": 128.09496,
    "M": 131.04049,
    "F": 147.06841,
    "P": 97.05276,
    "S": 87.03203,
    "T": 101.04768,
    "W": 186.07931,
    "Y": 163.06333,
    "V": 99.06841
}

dna_codon = {
    "AAA": "K",
    "AAC": "N",
    "AAG": "K",
    "AAT": "N",
    "ACA": "T",
    "ACC": "T",
    "ACG": "T",
    "ACT": "T",
    "AGA": "R",
    "AGC": "S",
    "AGG": "R",
    "AGT": "S",
    "ATA": "I",
    "ATC": "I",
    "ATG": "M",
    "ATT": "I",
    "CAA": "Q",
    "CAC": "H",
    "CAG": "Q",
    "CAT": "H",
    "CCA": "P",
    "CCC": "P",
    "CCG": "P",
    "CCT": "P",
    "CGA": "R",
    "CGC": "R",
    "CGG": "R",
    "CGT": "R",
    "CTA": "L",
    "CTC": "L",
    "CTG": "L",
    "CTT": "L",
    "GAA": "E",
    "GAC": "D",
    "GAG": "E",
    "GAT": "D",
    "GCA": "A",
    "GCC": "A",
    "GCG": "A",
    "GCT": "A",
    "GGA": "G",
    "GGC": "G",
    "GGG": "G",
    "GGT": "G",
    "GTA": "V",
    "GTC": "V",
    "GTG": "V",
    "GTT": "V",
    "TAA": "O",
    "TAC": "Y",
    "TAG": "O",
    "TAT": "Y",
    "TCA": "S",
    "TCC": "S",
    "TCG": "S",
    "TCT": "S",
    "TGA": "O",
    "TGC": "C",
    "TGG": "W",
    "TGT": "C",
    "TTA": "L",
    "TTC": "F",
    "TTG": "L",
    "TTT": "F"
}

def translate(dna_seq):
    if len(dna_seq) % 3 != 0 or "N" in dna_seq:
        print ("Invalid sequence: len = {}".format(len(dna_seq)))
        dna_seq = dna_seq[:-(len(dna_seq) % 3)]
    expected_len = int(len(dna_seq) / 3)
    ret = ""
    for i in range(expected_len):
        codon = dna_seq[i * 3:i * 3 + 3]
        # print("reading {} -> {} : {}".format(i * 3,i * 3 + 3, codon))
        amino_acid = dna_codon[codon]
        if amino_acid == "O":
            break
        ret = ret + dna_codon[codon]
    return ret

def calc_mass(prot_seq):
    ret = 0.0
    for c in prot_seq:
        ret = ret + mass_table[c]
        print(ret)
    return ret

def orf(dna_seq):
    ret = []
    i = 0
    while i * 3 < len(dna_seq):
        pept = translate(dna_seq[i * 3:])
        ret.append(pept)
        i = i + len(pept) + 1
    return ret
