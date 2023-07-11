import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox
from PyQt6.QtCore import Qt
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
            graph[anime_id] = {'name': anime_name, 'related': [anime.strip() for anime in related_anime]}

    return graph

class AnimeSearchWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Buscar Anime por DFS")

        self.layout = QVBoxLayout()

        self.titleLabel = QLabel("Buscar Anime:")
        self.layout.addWidget(self.titleLabel)

        self.searchTypeComboBox = QComboBox()
        self.searchTypeComboBox.addItem("Buscar por ID")
        self.searchTypeComboBox.addItem("Buscar por nombre")
        self.layout.addWidget(self.searchTypeComboBox)

        self.animeLineEdit = QLineEdit()
        self.layout.addWidget(self.animeLineEdit)

        self.resultLabel = QLabel()
        self.layout.addWidget(self.resultLabel)

        self.searchButton = QPushButton("Buscar Anime por el Archivo CSV")
        self.searchButton.clicked.connect(self.search_anime)
        self.layout.addWidget(self.searchButton)

        self.setLayout(self.layout)

    def search_anime(self):
        search_type = self.searchTypeComboBox.currentText()
        anime_query = self.animeLineEdit.text()

        # Ruta del archivo CSV de la biblioteca de anime
        csv_file = 'dataset/anime.csv'

        # Cargar la biblioteca de anime desde el archivo CSV
        anime_library = load_anime_library(csv_file)

        if search_type == "Buscar por ID":
            # Realizar la búsqueda por ID utilizando DFS
            result = search_anime_dfs(anime_library, anime_query, anime_query)
        else:
            # Realizar la búsqueda por nombre utilizando DFS
            result = None
            for anime_id, data in anime_library.items():
                if data['name'].lower() == anime_query.lower():
                    result = anime_id
                    break

        # Mostrar el resultado de la búsqueda
        if result:
            anime_name = anime_library[result]['name']
            self.resultLabel.setText(f"El anime '{anime_name}' fue encontrado en el archivo CSV.")
        else:
            self.resultLabel.setText(f"El anime con ID '{anime_query}' no fue encontrado en el archivo CSV.")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = AnimeSearchWindow()
    window.show()

    sys.exit(app.exec())


