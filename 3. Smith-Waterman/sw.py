# -*- coding: utf-8 -*-
import sys
#import numpy as np

def smithWaterman(s1,s2):
	score = 0	
	backtrack = []
	l__Max = 0
	c__Max = 0
	gap = input("Digite o valor do GAP: ")
	misMatch = input("Digite o Valor do MISMATCH: ")	
	match = input("Digite o valor do MATCH")
	tam__s1 = len(s1)
	tam__s2 = len(s2)
	#create matrix
	matriz = [[0 for x in range(tam__s1+1)] for x in range(tam__s2+1)]
	#first position in matrix gets 0
	matriz[0][0] = 0
	#fills the first row and colune
	for i in range(1, tam__s1+1):
		matriz[0][i] = matriz[0][i-1] + gap
	for i in range(1, tam__s2+1):
		matriz[i][0] = matriz[i-1][0] + gap

	#0 = diagonal, 1 = top, 2 = letf
	for x in range(1,tam__s2+1,1):
		tmp = []
		for y in range(1,tam__s1+1,1):
			values = []
			#diagonal value[0]
			if (s1[y-1] == s2[x-1]):
				values.append(matriz[x-1][y-1]+match)
			else:
				values.append(matriz[x-1][y-1]+misMatch)
			#top value[1]
			values.append(matriz[x-1][y]+gap)
			#left value[2]
			values.append(matriz[x][y-1]+gap)
			#max
			n = 0
			#values.append(0)
			if values[0] >= values[1] and values[0] >= values[2]:
				n = matriz[x][y] = values[0]
				t = 0
			elif values[1] >= values[0] and values[1] >= values[2]:
				n = matriz[x][y] = values[1]
				t = 1
			else:
				n = matriz[x][y] = values[2]
				t = 2		
			score = n
			tmp.append(t)
		backtrack.append(tmp[:])

	#BACKTRACK
	new__s1 = ""
	new__s2 = ""
	x = len(s2)-1
	y = len(s1)-1
	while (x >= 0 and y >= 0):
		idx = backtrack[x][y]
		#add diagonal s1 = s2
		if(idx == 0):
			new__s1 += s1[y]
			new__s2 += s2[x]
			x = x-1
			y = y-1
		#add top
		elif(idx == 1):
			new__s1 += "_"
			new__s2 += s2[x]
			x = x-1
		#add left
		elif(idx == 2):
			new__s1 += s1[y]
			new__s2 += "_"
			y = y-1

	if y == -1:	
		for i in range(x,-1,-1):
			new__s1 += "_"
			new__s2 += s2[i]
	elif x == -1:		
		for i in range(y,-1,-1):
			new__s2 += "_"
			new__s1 += s1[i]		

	#printing results
	print(new__s1[::-1])
	print(new__s2[::-1])
	print("Score: "+str(score))
	#write results in file
	f= open("out_sw.txt","w+")
	f.write(new__s1[::-1])
	f.write("\n")
	f.write(new__s2[::-1])
	f.write("\n")
	f.write("Score: "+str(score))

def read_fasta(arquivo):
	s1 = ''
	s2 = ''
	aux = []
	w_seq = 0
	try:
		with open(arquivo, 'r') as fasta:
			for line in fasta:
				if line.startswith('>'):
					w_seq += 1
					continue
				if w_seq == 1:
					s1 += line
				elif w_seq == 2:
					s2 += line
			s1 = s1.replace("\n", "")
			s1 = s1.replace("\r", "")
			s1 = s1.replace(".", "")
			s2 = s2.replace("\n", "")
			s2 = s2.replace("\r", "")
			s2 = s2.replace(".", "")
			smithWaterman(s1, s2)
	except IOError as fnf_error:
		print(fnf_error)
		print("\n")
		return False
	return True

def main():
	s1 = ""
	s2 = ""
	if sys.version_info.major == 2:
		fasta = raw_input("Digite o nome do arquivo (inclua .fasta):  ")
	elif sys.version_info.major == 3:
		fasta = input("Digite o nome do arquivo (inclua .fasta): ")

	while read_fasta(fasta) == False:
		if sys.version_info.major == 2:
			fasta = raw_input("Digite o nome do arquivo (inclua .fasta): ")
		elif sys.version_info.major == 3:
			fasta = input("Digite o nome do arquivo (inclua .fasta): ")

main()
