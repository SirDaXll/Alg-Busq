import csv

# Función para buscar anime en la biblioteca utilizando DFS
def search_anime_dfs(graph, start_node, target):
    visited = set()
    stack = [start_node]

    while stack:
        node = stack.pop()
        visited.add(node)

        # Verificar si el nodo actual es el anime objetivo
        if node == target:
            return node

        # Obtener los vecinos del nodo actual
        neighbors = graph.get(node, [])

        # Agregar los vecinos no visitados a la pila
        for neighbor in neighbors:
            if neighbor not in visited:
                stack.append(neighbor)

    # Si no se encuentra el anime objetivo
    return None

# Función para cargar la biblioteca de anime desde el archivo CSV
def load_anime_library(csv_file):
    graph = {}

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            anime_id = row['anime_id']
            anime_name = row['name']
            related_anime = row['genre'].split(',')
            graph[anime_id] = [anime.strip() for anime in related_anime]

    return graph

if __name__ == '__main__':
    # Ruta del archivo CSV de la biblioteca de anime
    csv_file = 'Dataset/anime.csv'

    # Cargar la biblioteca de anime desde el archivo CSV
    anime_library = load_anime_library(csv_file)

    # Obtener el anime de búsqueda desde la entrada del usuario
    anime_query = input("Ingrese el nombre del anime a buscar: ")

    # Realizar la búsqueda utilizando DFS
    result = search_anime_dfs(anime_library, 'One Piece', anime_query)

    # Mostrar el resultado de la búsqueda
    if result:
        print(f"El anime '{result}' fue encontrado en el archivo CSV.")
    else:
        print(f"El anime '{anime_query}' no fue encontrado en el archivo CSV.")
