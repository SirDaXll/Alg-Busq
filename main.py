import sys
from PyQt6.QtWidgets import QApplication
from backend.BFS import MainWindow as bfs
from backend.DFS import AnimeSearchWindow
from backend.linearSearch import MainWindow as ls

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    ventana_num = input("Ingrese el número del algoritmo que desea abrir (1 = BFS; 2 = DFS; 3 = Búsqueda Lineal): ")
    
    if ventana_num == "1":
        ventana = bfs()
    elif ventana_num == "2":
        ventana = AnimeSearchWindow()
    elif ventana_num == "3":
        ventana = ls()
    else:
        print("Número de algoritmo no válido.")
        sys.exit(1)
    
    ventana.show()
    sys.exit(app.exec())