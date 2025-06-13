# Clase que representa un grafo, dirigido o no dirigido, mediante un diccionario de adyacencia
class Grafo:
    def __init__(self, es_dirigido=False):
        # Inicializa el grafo como vacío y define si es dirigido
        self.vertices = {}  # Diccionario para representar el grafo
        self.es_dirigido = es_dirigido

    def agregar_vertice(self, vertice):
        # Agrega un vértice si no existe ya
        if vertice not in self.vertices:
            self.vertices[vertice] = []  # Inicializa la lista de vecinos

    def agregar_arista(self, u, v, peso=1):
        # Agrega una arista entre dos vértices (y los crea si no existen)
        if u not in self.vertices:
            self.agregar_vertice(u)
        if v not in self.vertices:
            self.agregar_vertice(v)

        if not self._existe_vecino(u, v):
            self.vertices[u] += [(v, peso)]

        # Si el grafo no es dirigido, se agrega la arista inversa    
        if not self.es_dirigido:
            if not self._existe_vecino(v, u):
                self.vertices[v] += [(u, peso)]

    def _existe_vecino(self, u, v):
        for vecino, _ in self.vertices.get(u, []):
            if vecino == v:
                return True
        return False

    def obtener_vecinos(self, vertice):
        # Devuelve la lista de vecinos de un vértice, o lista vacía si no existe
        if vertice in self.vertices:
            return [v for v, _ in self.vertices[vertice]]
        return []

    def existe_arista(self, u, v):
        # Verifica si existe una arista de u a v
        return self._existe_vecino(u, v)