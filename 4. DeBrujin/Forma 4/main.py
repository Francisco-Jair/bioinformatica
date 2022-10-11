from collections import defaultdict

def solve(k, kmers):
    graph = defaultdict(list)

    for kmer in kmers:
        startV = kmer[0:k-1]
        finalV = kmer[1:]
        graph[startV].append(finalV)

    gIn = {}
    gOut = {}
    for v in graph:
        gIn[v] = gOut[v] = 0

        for vertice in graph[v]:
            gIn[vertice] = gOut[vertice] = 0

    for v in graph:
        gOut[v] = len(graph[v])
        for next in graph[v]:
            gIn[next] += 1

    isZero = True
    notZero = []
    for vertice in gIn:
        if(gIn[vertice] != gOut[vertice]):
            isZero = False
            if(len(notZero) > 2):
                break
            else:
                notZero.append(vertice)

    isEulerian = False
    startV = ""

    if(isZero == True):
        isEulerian = True
        if(len(gIn) > 0):
            startV = gIn[0]
        else:
            startV = gOut[0]
    else:
        if(len(notZero) == 2):
            notZero[1] = notZero[1]
            if(((gIn[notZero[0]] + gOut[notZero[0]]) == (gIn[notZero[1]] + gOut[notZero[1]])) and ((gIn[notZero[1]] + gOut[notZero[1]]) == 1)):
                isEulerian = True
                if(gIn[notZero[0]] >= gOut[notZero[0]]):
                    startV = notZero[1]
                else:
                    startV = notZero[0]

    if(isEulerian == True):
        stack = []
        ans = []
        u = startV
        while(gOut[u] > 0 or len(stack) > 0):
            if(gOut[u] == 0):
                ans.append(u)
                u = stack.pop()
            else:
                stack.append(u)
                v = graph[u].pop()
                gOut[u] = gOut[u] - 1
                gIn[v] = gIn[v] - 1
                u = v
        ans.append(startV)
    else:
        print("Error ao encontrar o caominho")
    ans.reverse()
    return ans


file_name = input("Digite o nome do arquivo: ")
k = int(input("Digite o valor de k: "))

with open(file_name, 'r') as file:
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

file_name = "k"+str(k)+"mer.txt"

with open(file_name, 'r') as txt_file:
    kmers = txt_file.readline().split(',')[:-1]

path = solve(len(kmers[0]), kmers)

remontado = path[0][:]

for i in range(1, len(path)):
    remontado += path[i][-1]

file = open('output.txt', 'w')
file.write(remontado)
file.close()
