import csv
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QFileDialog, QLineEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Búsqueda Lineal en archivo CSV")
        self.layout = QVBoxLayout()
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)
        
        self.label = QLabel("Haz clic en el botón para buscar en el archivo CSV")
        self.layout.addWidget(self.label)
        
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Valor a buscar")
        self.layout.addWidget(self.search_input)
        
        self.button = QPushButton("Buscar en archivo CSV")
        self.button.clicked.connect(self.linear_search)
        self.layout.addWidget(self.button)
        
    def linear_search(self):
        file_path = "dataset/anime.csv"  # Ruta predeterminada del archivo CSV
        
        if file_path:
            with open(file_path, "r", encoding="utf-8-sig") as file:
                csv_reader = csv.reader(file)
                data = list(csv_reader)
            
            search_value = self.search_input.text()  # El valor que deseas buscar
            
            # Realizar la búsqueda lineal
            result = self.linear_search_value(data, search_value)
            
            if result:
                self.label.setText(f"El valor '{search_value}' fue encontrado en el archivo CSV.")
            else:
                self.label.setText(f"El valor '{search_value}' no fue encontrado en el archivo CSV.")
        else:
            self.label.setText("No se seleccionó ningún archivo CSV.")
    
    def linear_search_value(self, data, search_value):
        for row in data:
            if search_value in row:
                # El valor buscado fue encontrado en el archivo CSV
                return True
        
        # El valor buscado no está presente en el archivo CSV
        return False
        

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
