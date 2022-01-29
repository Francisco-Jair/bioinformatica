#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Fasta_r:
	def __init__(self):
		self.data = []
		self.k = 0
		self.d = 0

	def setFile(self, file):
		i = 0
		try:
			with open(file, 'r') as fasta:
				for line in fasta:
					#print(line)
					if i == 0:
						line = line.replace("(", "")
						line = line.replace(")", "")
						vet = line.split(",")
						self.k, self.d = vet[0], vet[1]
						i+=1
						continue
					line = line.replace("[", "")	
					line = line.replace("]", "")	
					line = line.replace(" ", "")	
					line = line.replace("'", "")
					vet = line.split(',')
					for v in vet:
						print(v)	
						self.data.append(v)
		except IOError as fnf_error:
			print(fnf_error)
			print("\n")
			return False
		return True	

	def getData(self):
		return self.data

	def getK(self):
		return self.k

	def getD(self):
		return self.d