dna = open('dna.txt','r')

date = dna.readline()
rna = ""

for i in date:

    if i == 'T':
        rna+="A"
    elif i == 'G':
        rna +="C"
    elif i == 'C':
        rna+="G"
    elif i == "A":
        rna+="U"


saveRna = open('rna.txt', 'w')
saveRna.write(rna)
saveRna.close()


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