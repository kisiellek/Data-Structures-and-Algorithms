# 1. Wykonaj DFS, zapisując dla każdego wierzchołka czas odwiedzenia.
# 2. Dla każdego wierzchołka oblicz (to się dzieje na wyjściu z rekurencji, dlatego przy wejściu najpierw wpisujemy do low(v) d(v)):
#    low(v) = min(d(v), min d(u), min low(w))
# gdzie:
# u - jest wierzchołkiem osiągalnym krawędzią wsteczną
# krawędź wsteczna to krawędź łącząca v z wierzchołkiem, który już wcześniej był odwiedzony
# w - jest dzieckiem v w drzewie DFS
# 3. Mosty to krawędzie {v, parent(v}, gdzie d(v) = low(v) | mosty nie leżą na żadnym cyklu prostym.

# Najpierw wpisujemy d(v), potem patrzymy na krawędzie wsteczne i przy powrocie min low(w)
# Tuż przed powrotem z rekurencji jeżeli d(v) == low(v) to mamy most (v wraz z parent(v) - no i ten parent musi jeszcze istnieć)

# O(V + E) - chyba
def bridge (G):
    n=len(G)
    parent=[None for i in range (n)]
    d=[float('inf') for i in range(n)]
    low = [float('inf') for i in range(n)]
    bridges=[]
    time=0

    def DFSVisit(G,u):
        nonlocal time
        d[u]=time
        low[u]=time
        time+=1

        for v in G[u]:
            if d[v]==float('inf'):       #not visited[v]:
                parent[v]=u
                low[u]=min(low[u], DFSVisit(G,v))
            elif v!=parent[u]:
                low[u]=min(low[u], d[v])
        # time+=1 - czas przetworzenia
        if low[u] == d[u] and parent[u] != None:
            bridges.append((u, parent[u]))

        return low[u]

    for u in range(n):
        if d[u] == float('inf'):
            DFSVisit(G, u)

    return bridges

G = [
    [1,4],
    [0,2,3],
    [1,3],
    [1,2],
    [0],
    [4,6],
    [4,5]
]

print(bridge(G))