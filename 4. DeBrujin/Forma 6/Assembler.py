from collections import defaultdict

class Remontagem():
    def __init__(self, kdmers, k , d):
        self.kdmers = kdmers
        self.k = int(k)
        self.d = int(d)
        self.construirGrafo()

    def construirGrafo(self):
        self.grafo = []
        self.dict_lista_adj = defaultdict(list)
        self.dict_arestas = {}

        
        for tupla in self.kdmers:
            vertice_origem = tupla[0][0:self.k-1] + tupla[1][0:self.k-1]
            aresta = tupla[0] + tupla[1]
            vertice_destino = tupla[0][1:] + tupla[1][1:]
            self.grafo.append((vertice_origem, aresta, vertice_destino))
            self.dict_lista_adj[vertice_origem].append(vertice_destino)
            self.dict_arestas[vertice_origem + vertice_destino] = aresta
            
        

        self.gerarListaAdjacencia()
        self.gerarCaminhosEulerianos()

    def getGrafo(self):
        return self.grafo

    def gerarListaAdjacencia(self):
        lista_adj = ""
        for vertice_chave in self.dict_lista_adj:
            lista_adj += vertice_chave + " -> "
            lista_vertices = self.dict_lista_adj[vertice_chave]
            for vertice in lista_vertices:
                lista_adj += vertice + " -> "
            lista_adj += "\n"

    
    def getListaAdjacencia(self):
        return self.dict_lista_adj
    
    def gerarCaminhosEulerianos(self):
        self.existeCaminhoEuleriano = False

        self.graus_entrada, self.graus_saida = {}, {}
        dict_lista_adj = self.getListaAdjacencia()

        for vertice_chave in dict_lista_adj:
            self.graus_saida[vertice_chave], self.graus_entrada[vertice_chave] = 0, 0
            lista_vertices = dict_lista_adj[vertice_chave]
            for vertice in lista_vertices:
                self.graus_saida[vertice], self.graus_entrada[vertice] = 0, 0
        
        for vertice_chave in dict_lista_adj:
            lista_vizinhos = dict_lista_adj[vertice_chave]
            self.graus_saida[vertice_chave] = len(lista_vizinhos)
            for vizinho in lista_vizinhos:
                self.graus_entrada[vizinho] += 1

        todos_tem_mesmo_grau = True
        qte_vertices_grau_diferente = 0
        vertices_grau_diferente = []

        for vertice in self.graus_entrada:
            if (self.graus_entrada[vertice] != self.graus_saida[vertice]):
                todos_tem_mesmo_grau = False
                if (qte_vertices_grau_diferente > 2):
                    break
                else:
                    vertices_grau_diferente.append(vertice)
                    qte_vertices_grau_diferente += 1
        
        vertice_inicio = ""

        if (todos_tem_mesmo_grau == True):
            self.existeCaminhoEuleriano = True
            if (len(self.graus_entrada) > 0):
                vertice_inicio = self.graus_entrada.keys()[0]
            else:
                vertice_inicio = self.graus_saida.keys()[0]
        else:
            if (qte_vertices_grau_diferente == 2):
                vertice1, vertice2 = vertices_grau_diferente[0], vertices_grau_diferente[1]
                if ((self.graus_saida[vertice1] + self.graus_entrada[vertice1]) == 1) and ((self.graus_entrada[vertice2] + self.graus_saida[vertice2]) == 1):
                    self.existeCaminhoEuleriano = True
                    if (self.graus_saida[vertice1] > self.graus_entrada[vertice1]):
                        vertice_inicio = vertice1[:]
                    else:
                        vertice_inicio = vertice2[:]
        
        if (self.existeCaminhoEuleriano == True):
            pilha, self.circuito = [], []
            vertice_corrente = vertice_inicio
            while(True):
                if(self.graus_saida[vertice_corrente] == 0 and len(pilha) == 0):
                    break
                else:
                    if(self.graus_saida[vertice_corrente] == 0):
                        self.circuito.append(vertice_corrente)
                        vertice_corrente = pilha.pop()
                    else:
                        pilha.append(vertice_corrente)
                        vizinho = self.dict_lista_adj[vertice_corrente].pop()
                        self.graus_saida[vertice_corrente] -= 1
                        self.graus_entrada[vizinho] -= 1
                        vertice_corrente = vizinho[:]
            
            self.circuito.append(vertice_inicio)
            self.circuito = self.circuito[::-1]
            caminho_euleriano = vertice_inicio[:]
            tam_caminho = len(self.circuito)
            for i in range(1, tam_caminho - 1):
                caminho_euleriano += " -> " + self.circuito[i]
            caminho_euleriano += " -> " + self.circuito[tam_caminho - 1]

            self.reconstruirSequencia()
    
    def reconstruirSequencia(self):
        arestas, tam_circuito = [], len(self.circuito) 
        for i in range(tam_circuito):
            if(i < tam_circuito - 1):
                chave = self.circuito[i] + self.circuito[i + 1]
                arestas.append(self.dict_arestas[chave])
        
        len_arestas = len(arestas)
        self.sequencia = arestas[0][:self.k]
        sufixos = ''
        for i in range(1, len_arestas):
            if i == (len_arestas - self.d - 1):
                sufixos += arestas[len_arestas - self.d - 1][self.k:self.k + self.d]
            if self.k < self.d:
                if i > (len_arestas - self.d - 1):
                    sufixos += arestas[i][-1]
            self.sequencia += arestas[i][:self.k][-1]

        self.sequencia += sufixos

        if self.k >= self.d:
            self.sequencia += arestas[-1][self.k:]

        arq = open('OUTPUT.fasta', 'w')
        arq.write(self.sequencia)
        arq.close()

    def existeEuleriano(self):
        return self.existeCaminhoEuleriano

    def getCircuito(self):
        return self.circuito

    def getSequencia(self):
        return self.sequencia


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
        print(k)
        print(d)
        par.append(k)
        par.append(d)
    else:
        aux1 += linha.rstrip("\n")
       
seq.append(aux1)
f.close()
f = open("k" + par[0] + "d" + par[1] +"mer.txt", 'r') 
lines = f.readlines() 

kdmer = []
valores = []

for line in lines:
    if line.find('>') == 0: 
        line = line.rstrip("\n")
        line = line.split("=")
        k = line[1]
        k = k.rstrip("d")
        d = line[2]
        valores.append(k)
        valores.append(d)
    else:
        lista = line.split(",")
        for par in lista:
            par = par.replace("[", "")
            par = par.replace("]", "")
            par = par.replace("'", "")
            par = par.replace(" ", "")
            aux = par.split("|")
            kdmer.append(aux)

k = valores[0]
d = valores[1]

grafo = Remontagem(kdmer, k, d)


if (grafo.existeEuleriano()):
    if (grafo.getSequencia() == seq[0]):
        print('\nSequência remontada nos arquivos:\n\t OUTPUT.fasta\n')
    else:
        print('Falha: foi gerada uma sequência diferente da original.')
        print('Tamanho da sequência original: %d' % len(seq[0]))
        print('Tamanho da sequência reconstruída: %d' % len(grafo.getSequencia()))
else:
    print('Não há caminho euleriano!')