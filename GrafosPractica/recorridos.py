from collections import deque

# Inserta un elemento al final de una lista
def insertar_final(lista, elemento):
    nueva = [None] * (len(lista) + 1)
    for i in range(len(lista)):
        nueva[i] = lista[i]
    nueva[len(lista)] = elemento
    return nueva

# Realiza un recorrido en anchura (BFS) desde un vértice inicial
def bfs(grafo, inicio):
    visitados = set()
    orden = []
    cola = deque()
    cola.append(inicio)

    while len(cola) > 0:
        actual = cola.popleft()
        if actual not in visitados:
            orden = insertar_final(orden, actual)
            visitados.add(actual)
            vecinos = grafo.obtener_vecinos(actual)
            for i in range(len(vecinos)):
                vecino = vecinos[i]
                if vecino not in visitados:
                    cola.append(vecino)
    return orden

# Realiza un recorrido en profundidad (DFS) desde un vértice inicial
def dfs(grafo, inicio):
    visitados = set()
    orden = []

# Función auxiliar recursiva
    def dfs_rec(v):
        nonlocal orden
        visitados.add(v)
        orden = insertar_final(orden, v)
        vecinos = grafo.obtener_vecinos(v)
        for i in range(len(vecinos)):
            vecino = vecinos[i]
            if vecino not in visitados:
                dfs_rec(vecino)

    if inicio in grafo.vertices:
        dfs_rec(inicio)
    return orden