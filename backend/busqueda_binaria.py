import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox

def busqueda_binaria(animes, objetivo):
    primero = 0
    ultimo = len(animes) - 1
    
    while primero <= ultimo:
        medio = (primero + ultimo) // 2
        anime_actual = animes[medio][0]  # Extraemos el nombre del anime
        
        if anime_actual == objetivo:
            return animes[medio]
        elif anime_actual < objetivo:
            primero = medio + 1
        else:
            ultimo = medio - 1
    
    return None

def buscar_anime():
    anime_buscado = entry.text()
    resultado = busqueda_binaria(base_de_datos, anime_buscado)

    if resultado:
        nombre, clasificacion = resultado
        QMessageBox.information(window, "Búsqueda binaria de anime", f"Se ha encontrado el anime '{nombre}' con clasificación '{clasificacion}'.")
    else:
        QMessageBox.information(window, "Búsqueda binaria de anime", "No se ha encontrado el anime.")

# Crear la aplicación
app = QApplication(sys.argv)

# Crear la ventana principal
window = QWidget()
window.setWindowTitle("Búsqueda binaria de anime")

# Crear etiqueta y entrada de texto
label = QLabel("Ingrese el nombre del anime:", window)
label.move(20, 20)
entry = QLineEdit(window)
entry.move(20, 50)

# Crear botón
button = QPushButton("Buscar", window)
button.move(20, 80)
button.clicked.connect(buscar_anime)

# Definir la base de datos
base_de_datos = [
    ("One Piece", "A"),
    ("Attack on Titan", "A+"),
    ("Naruto", "B"),
    ("My Hero Academia", "A"),
    ("Demon Slayer", "A+"),
    ("One Punch Man", "A-"),
    ("Fullmetal Alchemist", "A")
]

# Mostrar la ventana
window.setGeometry(100, 100, 300, 150)
window.show()

# Ejecutar la aplicación
sys.exit(app.exec())