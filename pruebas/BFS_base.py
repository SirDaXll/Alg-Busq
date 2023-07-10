import csv
from collections import deque
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QFileDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BFS en archivo CSV")
        self.layout = QVBoxLayout()
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)
        
        self.label = QLabel("Haz clic en el botón para buscar en anchura en el archivo CSV")
        self.layout.addWidget(self.label)
        
        self.button = QPushButton("Buscar en archivo CSV")
        self.button.clicked.connect(self.bfs_search)
        self.layout.addWidget(self.button)
        
    def bfs_search(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Seleccionar archivo CSV", "", "CSV Files (*.csv)")
        
        if file_path:
            with open(file_path, "r", encoding="utf-8-sig") as file:

                csv_reader = csv.reader(file)
                graph = list(csv_reader)
            
            start_node = (0, 0)  # Definir el nodo inicial (fila, columna)
            queue = deque([start_node])
            visited = set()
            
            while queue:
                node = queue.popleft()
                row, col = node
                
                # Verificar si el nodo actual ya ha sido visitado
                if node in visited:
                    continue
                
                # Obtener el valor en el nodo actual
                value = graph[row][col]
                
                # Realizar la acción deseada en el valor (por ejemplo, imprimirlo)
                print(value)
                
                # Marcar el nodo actual como visitado
                visited.add(node)
                
                # Agregar los nodos vecinos (hijos) al final de la cola
                if row + 1 < len(graph):
                    queue.append((row + 1, col))  # Nodo inferior
                if col + 1 < len(graph[row]):
                    queue.append((row, col + 1))  # Nodo derecho
                    
            self.label.setText("Búsqueda en anchura completada.")
        else:
            self.label.setText("No se seleccionó ningún archivo CSV.")
        

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
