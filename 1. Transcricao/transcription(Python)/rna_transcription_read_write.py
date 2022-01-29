from string import maketrans 

str_in = open('input.txt', 'r').readline()
str_out = open('output.txt', 'w')
in_FDna = "GCTA"
out_Rna = "CGAU"
transc = maketrans(in_FDna, out_Rna)

str_out.write(str_in.translate(transc))
