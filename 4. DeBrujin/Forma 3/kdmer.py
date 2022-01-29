def readFasta():

    arquivo = input("Digite o nome do arquivo: ")
    dic = {}
    with open(arquivo, 'r') as fasta:
        for linha in fasta:
            if not linha.startswith('>'):
                dic['sequence'] = linha
            else:
                linha = linha.strip('>k=')
                linha = linha.split('d=')
                dic['k'] = int(linha[0])
                dic['d'] = int(linha[1])
        return dic
    
def kdMer(sequence, k, d):
    try:
        with open("k"+str(k)+"d"+str(d)+"mer.txt", "w") as file:
            tam =len(sequence)
            kdmers = [sequence[i:(i+k)]+"|"+sequence[(i+k+d):(i+d+k+k)] for i in range(0, tam-(k+d+(k-1)))]
            kdmers.sort()
            file.write('[')
            for i, kdmer in enumerate(kdmers):
                if i != 0:
                    file.write(',')
                file.write(kdmer)
            file.write(']')
            print("Arquivo "+"k"+str(k)+"d"+str(d)+"mer.txt"+" criado com sucesso!")
            return kdmers
    except Exception:
        print("Ocorreu algum problema com a criação do arquivo "+"k"+str(k)+"d"+str(d)+"mer.txt!")
        return None

if __name__ == "__main__":
    info = readFasta()
    kdMer(info['sequence'], info['k'], info['d'])