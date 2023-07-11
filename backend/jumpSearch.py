import csv
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QFileDialog, QLineEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Búsqueda por Salto en archivo CSV")
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
        self.button.clicked.connect(self.jump_search)
        self.layout.addWidget(self.button)
        
    def jump_search(self):
        file_path = "dataset/anime.csv"  # Ruta predeterminada del archivo CSV
        
        if file_path:
            with open(file_path, "r", encoding="utf-8-sig") as file:
                csv_reader = csv.reader(file)
                data = list(csv_reader)
            
            search_value = self.search_input.text()  # El valor que deseas buscar
            
            # Realizar la búsqueda por salto
            result = self.jump_search_value(data, search_value)
            
            if result:
                self.label.setText(f"El valor '{search_value}' fue encontrado en el archivo CSV.")
            else:
                self.label.setText(f"El valor '{search_value}' no fue encontrado en el archivo CSV.")
        else:
            self.label.setText("No se seleccionó ningún archivo CSV.")
    
    def jump_search_value(self, data, search_value):
        # Convertir el valor de búsqueda a entero
        search_value = int(search_value)
        
        # Obtener la longitud del archivo CSV
        length = len(data)
        
        # Calcular el salto (step)
        step = int(length ** 0.5)
        
        prev = 0
        while int(data[min(step, length) - 1][0]) < search_value:
            prev = step
            step += int(length ** 0.5)
            if prev >= length:
                # El valor buscado no está presente en el archivo CSV
                return False
        
        # Realizar una búsqueda lineal en el rango encontrado
        for i in range(prev, min(step, length)):
            if int(data[i][0]) == search_value:
                # El valor buscado fue encontrado en el archivo CSV
                return True
            elif int(data[i][0]) > search_value:
                # El valor buscado no está presente en el archivo CSV
                return False
        
        # El valor buscado no está presente en el archivo CSV
        return False
        

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
