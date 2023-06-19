import sys
import pandas
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QWidget, QTableWidget, QTableWidgetItem, QPushButton
from PyQt6.QtGui import QIcon

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Base de datos de anime')
        self.resize(1200, 400)

        # Importar el dataset
        self.ds = pandas.read_csv('dataset/anime.csv')

        # Widgets de búsqueda
        #self.id = QLineEdit()
        #self.name = QComboBox()
        self.genre = QComboBox()
        self.type = QComboBox()
        #self.episodes = QLineEdit()
        #self.rating = QLineEdit()
        #self.members = QLineEdit()

        # Configurar opciones de ComboBox
        self.genre.addItem('Todos')
        self.ds['genre'] = self.ds['genre'].astype(str)
        self.genre.addItems(self.ds['genre'].unique())

        self.type.addItem('Todos')
        self.ds['type'] = self.ds['type'].astype(str)
        self.type.addItems(self.ds['type'].unique())

        # Botón de búsqueda
        self.searchButton = QPushButton('Buscar')
        self.searchButton.clicked.connect(self.search)

        # Tabla de resultados
        self.resultTable = QTableWidget()
        self.resultTable.setColumnCount(7)
        self.resultTable.setHorizontalHeaderLabels(['ID', 'Anime', 'Género', 'Tipo', 'Episodios', 'Puntuación', 'Miembros'])
        self.resultTable.setRowCount(0)

        # Layouts
        search = QVBoxLayout()
        #search.addWidget(QLabel('ID:'))
        #search.addWidget(self.id)
        #search.addWidget(QLabel('Anime:'))
        #search.addWidget(self.name)
        search.addWidget(QLabel('Género:'))
        search.addWidget(self.genre)
        search.addWidget(QLabel('Tipo:'))
        search.addWidget(self.type)
        #search.addWidget(QLabel('Episodios:'))
        #search.addWidget(self.episodes)
        #search.addWidget(QLabel('Puntuación:'))
        #search.addWidget(self.rating)
        #search.addWidget(QLabel('Miembros:'))
        #search.addWidget(self.members)
        search.addWidget(self.searchButton)

        main = QHBoxLayout()
        main.addLayout(search)
        main.addWidget(self.resultTable)

        self.setLayout(main)

    def search(self):
        #id = self.id.text().lower()
        #name = self.name.text()
        genre = self.genre.currentText()
        type = self.type.currentText()

        # Filtrar el Data Set
        query = f'id.str.lower().str.contains("{id}")'
        if genre != 'Todos':
            query += f' and genre == "{genre}"'
        if type != 'Todos':
            query += f' and type == "{type}"'

        # Optimizar tabla según filtro
        filtro = self.ds.query(query)
        filtro = filtro.dropna()
        filtro = filtro.reset_index(drop = True)

        # Mostrar los resultados de la tabla
        self.resultTable.setRowCount(len(filtro))
        for i, row in filtro.iterrows():
            idItem = QTableWidgetItem(row['anime_id'])
            nameItem = QTableWidgetItem(row['name'])
            genreItem = QTableWidgetItem(str(row['genre']))
            typeItem = QTableWidgetItem(str(row['type']))
            episodesItem = QTableWidgetItem(str(row['episodes']))
            ratingItem = QTableWidgetItem(str(row['rating']))
            membersItem = QTableWidgetItem(str(row['members']))

            self.resultTable.setItem(i, 0, idItem)
            self.resultTable.setItem(i, 1, nameItem)
            self.resultTable.setItem(i, 2, genreItem)
            self.resultTable.setItem(i, 3, typeItem)
            self.resultTable.setItem(i, 4, episodesItem)
            self.resultTable.setItem(i, 5, ratingItem)
            self.resultTable.setItem(i, 6, membersItem)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    icon = QIcon('nota.png')
    ventana.setWindowIcon(icon)
    ventana.show()
    app.exec()
