import csv
# 'deque' (double-ended queue) se utiliza para implementar una cola eficiente en el algoritmo de búsqueda en anchura, permitiendo agregar
# y eliminar nodos de manera eficiente tanto al principio como al final de la cola
from collections import deque
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BFS en archivo CSV")
        self.layout = QVBoxLayout()
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)
        
        # Crear una etiqueta para mostrar mensajes
        self.label = QLabel("Haz clic en el botón para buscar en anchura en el archivo CSV")
        self.layout.addWidget(self.label)
        
        # Crear un campo de entrada para el valor a buscar
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Valor a buscar")
        self.layout.addWidget(self.search_input)
        
        # Crear un botón para iniciar la búsqueda
        self.button = QPushButton("Buscar en archivo CSV")
        self.button.clicked.connect(self.bfs_search)
        self.layout.addWidget(self.button)
        
    def bfs_search(self):
        file_path = "dataset/anime.csv"  # Ruta predeterminada del archivo CSV
        
        # Abrir el archivo CSV y leer los datos en una lista de listas
        with open(file_path, "r", encoding="utf-8-sig") as file:
            csv_reader = csv.reader(file)
            graph = list(csv_reader)
        
        start_node = (0, 0)  # Definir el nodo inicial (fila, columna)
        queue = deque([start_node])  # Crear una cola con el nodo inicial
        visited = set()  # Conjunto para almacenar nodos visitados durante la búsqueda
        
        search_value = self.search_input.text()  # Obtener el valor a buscar del campo de entrada
        found = False  # Variable para rastrear si se encontró el valor buscado
        
        while queue:
            node = queue.popleft()  # Extraer el nodo de la cabeza de la cola
            row, col = node
            
            # Verificar si el nodo actual ya ha sido visitado
            if node in visited:
                continue
            
            # Obtener el valor en el nodo actual
            value = graph[row][col]
            
            # Realizar la acción deseada en el valor (por ejemplo, imprimirlo)
            print(value)
            
            # Verificar si se encontró el valor buscado
            if value == search_value:
                found = True
                break
            
            # Marcar el nodo actual como visitado
            visited.add(node)
            
            # Agregar los nodos vecinos (hijos) al final de la cola
            if row + 1 < len(graph):
                queue.append((row + 1, col))  # Nodo inferior
            if col + 1 < len(graph[row]):
                queue.append((row, col + 1))  # Nodo derecho
        
        # Actualizar la etiqueta con el resultado de la búsqueda
        if found:
            self.label.setText(f"El valor '{search_value}' fue encontrado en el archivo CSV.")
        else:
            self.label.setText(f"El valor '{search_value}' no fue encontrado en el archivo CSV.")
        

if __name__ == "__main__":
    app = QApplication([])  # Crear una instancia de la aplicación PyQt
    window = MainWindow()  # Crear una instancia de la ventana principal
    window.show()  # Mostrar la ventana principal
    app.exec()  # Iniciar el bucle de eventos de la aplicación
