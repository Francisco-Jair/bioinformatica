import numpy as np
from collections import defaultdict
def composicao(seq,k,d):
    comp = []
    k,d = int(k), int(d)
    tam = len(seq)
    for i in range(tam):
        elem_1 =  seq[i:i+k]
        elem_2 = seq[i+k+d:i+2*k+d]
        if (len(elem_1) < k or len(elem_2.rstrip("\t")) < k):
            break
        else:
            comp.append((elem_1, elem_2))
    comp.sort()
    aux = []
    nome = "k" + str(k) + "d" + str(d) + "mer.txt"
    arq = open(nome , "w")
    arq.write(">k=" + str(k) + "d=" + str(d) + "\n")
    for par in comp:
        aux.append(par[0] + "|" + par[1])
    arq.write(str(aux))
    arq.close()
    print("\nComposição gerada no arquivo " + nome)
    print()
   
arquivo = 'INPUT.fasta'
f = open(arquivo, 'r') 
linhas = f.readlines() 
aux1= ""
seq = []
par = [] 
for linha in linhas:
    if linha.find('>') == 0: 
        linha = linha.rstrip("\n")
        linha = linha.split("=")
        k = linha[1]
        k = k.rstrip("d")
        d = linha[2]
        par.append(k)
        par.append(d)
    else:
        aux1 += linha.rstrip("\n")
        
seq.append(aux1)
composicao(seq[0], par[0], par[1])
