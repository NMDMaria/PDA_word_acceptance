fin = open("date.in", "r")
N = int(fin.readline().strip())
aux = fin.readline().strip().split()
Q = [item for item in aux]
S = fin.readline().strip()
nrF = int(fin.readline().strip())
aux = fin.readline().strip().split()
F = [item for item in aux]
nrM = int(fin.readline().strip())

# $ = nimic
D = {}
for i in range(nrM):
    aux = fin.readline().strip().split()
    cine = aux[0]
    unde = aux[1]
    litera = aux[2]
    pop = aux[3]
    push = aux[4]

    if cine not in D:
        D.update({cine: {litera: (unde, pop, push)}})
    else:
        D[cine].update({litera: (unde, pop, push)})

# print(D)
word = fin.readline().strip()

stiva = []
flag = False


def parcurgere(stare, index):
    global D, stiva, F, word, flag
    # print(stiva, index, stare, stare in F, len(word) - 1)
    if (len(stiva) == 0 or stare in F) and index > len(word) - 1:
        print("accepted")
        flag = True
        return

    if stare in D:
        T = D[stare]
        litere = list(T.keys())
        for litera in litere:
            # print(T[litera])
            if litera == '$':
                if T['$'][2] != '$':
                    stiva.append(T['$'][2])
                parcurgere(T['$'][0], index)
                if T['$'][2] != '$':
                    stiva.pop(len(stiva) - 1)

            if index < len(word) and word[index] == litera:
                k = T[word[index]]
                if k[1] == '$':
                    if k[2] != '$':
                        stiva.append(k[2])
                    parcurgere(k[0], index + 1)
                    if k[2] != '$' and stiva[len(stiva) - 1] == k[2]:
                        stiva.pop(len(stiva) - 1)

                elif stiva[len(stiva) - 1] == k[1]:
                    stiva.pop(len(stiva) - 1)
                    if k[2] != '$':
                        stiva.append(k[2])
                    parcurgere(k[0], index + 1)
                    if k[2] != '$' and stiva[len(stiva) - 1] == k[2]:
                        stiva.pop(len(stiva) - 1)
                    stiva.append(k[1])


parcurgere(S, 0)
if flag is False:
    print("not accepted")