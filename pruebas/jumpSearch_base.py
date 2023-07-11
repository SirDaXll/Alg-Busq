import csv
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QFileDialog

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
        
        self.button = QPushButton("Buscar en archivo CSV")
        self.button.clicked.connect(self.jump_search)
        self.layout.addWidget(self.button)
        
    def jump_search(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Seleccionar archivo CSV", "", "CSV Files (*.csv)")
        
        if file_path:
            with open(file_path, "r") as file:
                csv_reader = csv.reader(file)
                data = list(csv_reader)
            
            search_value = "valor_a_buscar"  # El valor que deseas buscar
            
            # Obtener la longitud del archivo CSV
            length = len(data)
            
            # Calcular el salto (step)
            step = int(length ** 0.5)
            
            prev = 0
            while data[min(step, length) - 1][0] < search_value:
                prev = step
                step += int(length ** 0.5)
                if prev >= length:
                    # El valor buscado no está presente en el archivo CSV
                    self.label.setText("El valor buscado no está presente en el archivo CSV.")
                    return
            
            while data[prev][0] < search_value:
                prev += 1
                if prev == min(step, length):
                    # El valor buscado no está presente en el archivo CSV
                    self.label.setText("El valor buscado no está presente en el archivo CSV.")
                    return
            
            if data[prev][0] == search_value:
                # El valor buscado fue encontrado en el archivo CSV
                self.label.setText("El valor buscado fue encontrado en el archivo CSV.")
            else:
                # El valor buscado no está presente en el archivo CSV
                self.label.setText("El valor buscado no está presente en el archivo CSV.")
        else:
            self.label.setText("No se seleccionó ningún archivo CSV.")
        

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
