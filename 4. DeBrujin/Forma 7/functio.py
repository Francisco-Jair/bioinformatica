


def load_file(path):
    f = open(path, "r")
    arquivo = f.readlines()
    f.close()
    return arquivo


def processing_file(file):

    file = file[0].split(",")
    k = len(file[0])
    primeiro = None
    grafo = []
    for index, i in enumerate(file):
        # print(f". Adicionando parte... [{index+1}/{len(arquivo)}]")
        grafo.append((i[:-1], i[1:]))
    

    return grafo


def get_first_element_graph(graph):
    first = graph[[(sum(map(lambda x : 1 if x[1]==i[0] else 0,graph))==0) for i in graph].index(True)]
    primeiro = first[0]
    return primeiro


def solver(tamanhoGrafo, graph, nomeSaida, primeiro):
    resultado = ""

    for i in range(tamanhoGrafo-1):
    # print(f". Filtrando elemento do grafo: {i+1}/{tamanhoGrafo-1}")
    # Cria uma lista onde se filtra os elementos do grafo que são diferentes do elemento inicial.
        a = list(filter(lambda x: x[0] == primeiro, graph))
        try:
            # Elimina-se o elemento inicial da lista no grafo, pois o mesmo já foi usado.
            del(graph[graph.index(a[0])])
        except:
            print(graph)

        g = a[0]
        h = g[1]
        if i < tamanhoGrafo-1:
            resultado += primeiro[0]
        else:
            resultado += primeiro[0] + h
        primeiro = h

    with open(f"{nomeSaida}.txt", 'w') as arquivo:    
        arquivo.write(resultado)