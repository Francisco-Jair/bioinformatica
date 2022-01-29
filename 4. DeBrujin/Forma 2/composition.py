file_name = input("Digite o nome do arquivo: ")

with open(file_name, 'r') as file:
    k = int(file.readline().split('=')[1].replace("\n", ''))
    sequence = file.readlines()[0].replace("\n", '')

kmers = []

for i in range(len(sequence)):
    kmer = sequence[i:i+k]
    if (len(kmer) < k):
        break
    kmers.append(kmer)

kmers.sort()

file = open("k"+str(k)+"mer.txt", "w")
for kmer in kmers:
    file.write(kmer + ",")
file.close()