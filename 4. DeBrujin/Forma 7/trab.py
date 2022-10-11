from functio import load_file, processing_file, get_first_element_graph, solver


if __name__ == "__main__":
    #1. carregar arquivo
    arq = load_file("10000_k_25.txt")
    # arq = load_file("30000_k_50.txt")

    #2. 
    graph = processing_file(arq)

    #3. 
    first_element = get_first_element_graph(graph)
    tamanhoGrafo = len(graph)

    #4.
    solver(tamanhoGrafo, graph, "claudioMatheus", first_element)


