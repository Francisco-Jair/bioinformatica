geneticCode = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'L', 'UCG': 'L',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': 'ST', 'UAG': 'ST',
    'UGU': 'C', 'UGC': 'C', 'UGA': 'ST', 'UGG': 'W',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}

#AUGGGGGCAGGUCUUGAUGUAGCAACGACAGGGUUCUUAAAGCAGCAAAGAGUUGGCAGACGUUAG

rna = input("Entre com a fita de RNA: ").upper()

rnam = []

cont = 0
r = ""
for i in rna:
    if cont == 3:
        cont = 0
        rnam.append(r)
        r = ""

    r += i
    cont += 1
    

#print(rnam)
#rnam = rna.split('.')


iniciarT = False

for mensageiro in rnam:

    if "AUG" == mensageiro:
        iniciarT = True

    if "UAA" == mensageiro or "UAG" == mensageiro or "UGA" == mensageiro:
        iniciarT = False
        print(geneticCode[mensageiro])

    if iniciarT:
        print(geneticCode[mensageiro])
