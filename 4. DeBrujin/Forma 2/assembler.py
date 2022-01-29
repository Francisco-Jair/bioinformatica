from collections import defaultdict

def solve(k, kmers):
    graph = defaultdict(list)

    for kmer in kmers:
        start_v = kmer[0:k-1]
        final_vertice = kmer[1:]
        graph[start_v].append(final_vertice)

    grau_in = {}
    grau_out = {}
    for v in graph:
        grau_in[v] = grau_out[v] = 0

        for vertice in graph[v]:
            grau_in[vertice] = grau_out[vertice] = 0

    for v in graph:
        grau_out[v] = len(graph[v])
        for neighbor in graph[v]:
            grau_in[neighbor] += 1

    is_zero = True
    not_zero = []
    for vertice in grau_in:
        if(grau_in[vertice] != grau_out[vertice]):
            is_zero = False
            if(len(not_zero) > 2):
                break
            else:
                not_zero.append(vertice)

    is_eulerian = False
    start_v = ""

    if(is_zero == True):
        is_eulerian = True
        if(len(grau_in) > 0):
            start_v = grau_in[0]
        else:
            start_v = grau_out[0]
    else:
        if(len(not_zero) == 2):
            not_zero[1] = not_zero[1]
            if(((grau_in[not_zero[0]] + grau_out[not_zero[0]]) == (grau_in[not_zero[1]] + grau_out[not_zero[1]])) and ((grau_in[not_zero[1]] + grau_out[not_zero[1]]) == 1)):
                is_eulerian = True
                if(grau_in[not_zero[0]] >= grau_out[not_zero[0]]):
                    start_v = not_zero[1]
                else:
                    start_v = not_zero[0]

    if(is_eulerian == True):
        stack = []
        ans = []
        u = start_v
        while(grau_out[u] > 0 or len(stack) > 0):
            if(grau_out[u] == 0):
                ans.append(u)
                u = stack.pop()
            else:
                stack.append(u)
                v = graph[u].pop()
                grau_out[u] = grau_out[u] - 1
                grau_in[v] = grau_in[v] - 1
                u = v
        ans.append(start_v)
    else:
        print("Caminho Euleriano não encontrado!")
    ans.reverse()
    return ans


file_name = input("Digite o nome do arquivo: ")

with open(file_name, 'r') as txt_file:
    kmers = txt_file.readline().split(',')[:-1]

path = solve(len(kmers[0]), kmers)

remontado = path[0][:]

for i in range(1, len(path)):
    remontado += path[i][-1]

file = open('remontado.fasta', 'w')
file.write(remontado)
file.close()
