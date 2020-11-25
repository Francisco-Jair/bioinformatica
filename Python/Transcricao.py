#Transcrição de DNA

dna = input("Entre com o DNA: ")

dna = dna.upper()
dna_tras = []

for rna in list(dna):    

    if rna == 'T':
        dna_tras.append('U')
    elif rna != '.':
        dna_tras.append(rna)
        
dna = ''.join(dna_tras)

print(dna)

"""
No DNA temos as bases
T - A
C - G 

no RNA temos que

U - A
C - G 

Então para transformar uma fita de DNA em RNA fazemos
a troca do T pelo U somente
"""