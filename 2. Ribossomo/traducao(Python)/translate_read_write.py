# -*- coding: utf-8 -*-
import sys

def translate(seq): 

    geneticCode = {
	'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L', #UU
	'UCU':'S', 'UCC':'S', 'UCA':'L', 'UCG':'L', #UC
	'UAU':'Y', 'UAC':'Y', 'UAA':'ST', 'UAG':'ST', #UA
	'UGU':'C', 'UGC':'C', 'UGA':'ST', 'UGG':'W', #UG
	'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L', #CU
	'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P', #CC
	'CAU':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q', #CA
	'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', #CG
	'AUU':'I', 'AUC':'I', 'AUA':'I', 'AUG':'M', #AU
	'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T', #AC
	'AAU':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K', #AA
	'AGU':'S', 'AGC':'S', 'AGA':'A', 'AGG':'A', #AG
	'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V', #GU
	'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A', #GC
	'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E', #GA
	'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G' #GG
	}

    protein =""
    if len(seq)%3 == 0:
        for i in range(0, len(seq), 3):
            codon = seq[i:i + 3]
            protein += geneticCode[codon]
            #print(protein)
        return protein

def read_file(name):
	try:
	    with open(name, "r") as file:
	    	seq = file.read()
	except IOError as fnf_error:
		print(fnf_error)
		print("\n")
		return False

	seq = seq.replace("\n", "")  
	seq = seq.replace("\r", "")
	seq = seq.replace(".", "")
	print("\nmRna: " + seq)
	print("\n")
	print("Proteina: " + translate(seq))
	return True

def main():
	if sys.version_info.major == 2:
		name = raw_input("Digite o nome do arquivo com a sua extenção (.txt): ")
	elif sys.version_info.major == 3:
		name = input("Digite o nome do arquivo com a sua extenção (.txt): ")

	while read_file(name) == False:
		if sys.version_info.major == 2:
			name = raw_input("Digite o nome do arquivo com a sua extenção (.txt): ")
		elif sys.version_info.major == 3:
			name = input("Digite o nome do arquivo com a sua extenção (.txt): ")

main()
