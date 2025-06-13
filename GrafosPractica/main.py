from grafo import Grafo
from recorridos import bfs, dfs
from analisis import es_conexo, encontrar_camino

# EJERCICIO 1
print("\n--- Grafo No Dirigido (Mapas GPS) ---")
# Se crea una instancia de grafo no dirigido y se agregan vértices y aristas
g = Grafo()
for v in ['A', 'B', 'C', 'D', 'E']:
    g.agregar_vertice(v)

aristas = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]
for u, v in aristas:
    g.agregar_arista(u, v)

# Pruebas de operaciones basicas
print("Vecinos de A:", g.obtener_vecinos('A'))
print("Vecinos de D:", g.obtener_vecinos('D'))
print("Vecinos de F:", g.obtener_vecinos('F'))  # No existe

print("¿Existe arista A-C?", g.existe_arista('A', 'C'))
print("¿Existe arista A-D?", g.existe_arista('A', 'D'))

# Grafo dirigido
print("\n--- Grafo Dirigido ---")
gd = Grafo(es_dirigido=True)
for u, v in [('X', 'Y'), ('Y', 'Z'), ('X', 'Z')]:
    gd.agregar_arista(u, v)

print("Vecinos de X:", gd.obtener_vecinos('X'))
print("Vecinos de Y:", gd.obtener_vecinos('Y'))

# EJERCICIO 2
# BFS y DFS
print("\n--- BFS y DFS ---")
print("BFS desde A:", bfs(g, 'A'))
print("DFS desde A:", dfs(g, 'A'))

# Agregar un vértice desconexo
g.agregar_vertice('F')
print("BFS con F:", bfs(g, 'F'))  # solo F
print("DFS con F:", dfs(g, 'F'))  # solo F

# EJERCICIO 3
# Conectividad y rutas
print("\n--- Análisis del Grafo ---")
print("¿Es conexo?", es_conexo(g))
print("Camino de A a E:", encontrar_camino(g, 'A', 'E'))
print("Camino de A a Z (inexistente):", encontrar_camino(g, 'A', 'Z'))