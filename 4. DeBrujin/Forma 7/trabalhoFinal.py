import sys

print(sys.argv)

# Lendo arquivo
print("Lendo arquivo ...")
# filepath = sys.argv[1]

filepath = "10000_k_25.txt"
# filepath = "30000_k_50.txt"

f = open(filepath, "r")
arquivo = f.readlines()
f.close()

print("Processando arquivo ...")
arquivo = arquivo[0].split(",")
k = len(arquivo[0])
primeiro = None
grafo = []
for index,i in enumerate(arquivo):
    # print(f". Adicionando parte... [{index+1}/{len(arquivo)}]")
    grafo.append((i[:-1], i[1:]))

print("Obtendo primeiro elemento do grafo ...")
first = grafo[[(sum(map(lambda x : 1 if x[1]==i[0] else 0,grafo))==0) for i in grafo].index(True)]
primeiro = first[0]
print("Alocando vetor para armazenar resultado ...")
resultado = ""
tamanhoGrafo = len(grafo)
print(f"Processando grafo de tamanho = {tamanhoGrafo-1}")
for i in range(tamanhoGrafo-1):
    # print(f". Filtrando elemento do grafo: {i+1}/{tamanhoGrafo-1}")
    # Cria uma lista onde se filtra os elementos do grafo que são diferentes do elemento inicial.
    a = list(filter(lambda x: x[0] == primeiro, grafo))
    try:
        # Elimina-se o elemento inicial da lista no grafo, pois o mesmo já foi usado.
        del(grafo[grafo.index(a[0])])
    except:
        print(grafo)

    g = a[0]
    h = g[1]
    if i < tamanhoGrafo-1:
        resultado += primeiro[0]
    else:
        resultado += primeiro[0] + h
    primeiro = h

with open("cm.txt", 'w') as arquivo:    
    arquivo.write(resultado)
