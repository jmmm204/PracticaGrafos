from collections import deque

# Verifica si el grafo no dirigido es conexo usando DFS
def es_conexo(grafo):
    if not grafo.vertices:
        return True # Un grafo vacío se considera conexo

    visitados = set()
    inicio = next(iter(grafo.vertices))

    cola = deque()
    cola.append(inicio)

    while cola:
        actual = cola.popleft()
        if actual not in visitados:
            visitados.add(actual)
            for vecino in grafo.obtener_vecinos(actual):
                if vecino not in visitados:
                    cola.append(vecino)

    return len(visitados) == len(grafo.vertices)

# Busca un camino entre dos vértices usando BFS y reconstruye el trayecto
def encontrar_camino(grafo, inicio, fin):
    if inicio not in grafo.vertices or fin not in grafo.vertices:
        return []

    padres = {inicio: None}
    cola = deque()
    cola.append(inicio)

    while cola:
        actual = cola.popleft()
        if actual == fin:
            break
        for vecino in grafo.obtener_vecinos(actual):
            if vecino not in padres:
                padres[vecino] = actual
                cola.append(vecino)

    if fin not in padres:
        return [] # No hay camino

    # Reconstruye el camino desde el nodo fin hasta el inicio
    camino = []
    actual = fin
    while actual is not None:
        camino.insert(0, actual)
        actual = padres[actual]

    return camino