import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QLabel, QPushButton, QWidget
from ayuda import Ayuda
from error import Error
from resultado import Resultado
from resultadoError import resultadoError


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(400, 400)
        MainWindow.setMinimumSize(QtCore.QSize(400, 400))
        MainWindow.setMaximumSize(QtCore.QSize(400, 400))
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Spanish, QtCore.QLocale.Country.Chile))
        MainWindow.setDockOptions(QtWidgets.QMainWindow.DockOption.AllowTabbedDocks | QtWidgets.QMainWindow.DockOption.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 381, 16))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 381, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 90, 361, 22))
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 160, 381, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 190, 361, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 270, 381, 16))
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(20, 300, 361, 22))
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 350, 75, 24))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.mostrarResultado)

        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 10, 21, 21))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(self.mostrarAyuda)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Algoritmos para búsqueda en diccionario - Anime"))
        self.label.setText(_translate("MainWindow", "¡Bienvenido usuario!"))
        self.label_2.setText(_translate("MainWindow", "Seleccione el criterio que utilizará para buscar:"))
        self.comboBox.setCurrentText(_translate("MainWindow", "ID"))
        self.comboBox.setItemText(0, _translate("MainWindow", "ID"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Nombre"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Género"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Tipo"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Episodios"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Puntuación"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Miembros"))
        self.label_3.setText(_translate("MainWindow", "Ingrese una palabra o valor para buscar:"))
        self.label_4.setText(_translate("MainWindow", "Seleccione que algoritmo desea utilizar para su búsqueda:"))
        self.comboBox_2.setCurrentText(_translate("MainWindow", "Búsqueda binaria (listas)"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Búsqueda binaria (listas)"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Búsqueda en profundidad (DFS) (árboles)"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Búsqueda en anchura (BFS) (gráfos)"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Algoritmo 4"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Algoritmo 5"))
        self.pushButton.setText(_translate("MainWindow", "Buscar"))
        self.pushButton_2.setText(_translate("MainWindow", "?"))

    def mostrarAyuda(self):
        self.ayuda = Ayuda()
        self.ayuda.show()

    def mostrarError(self):
        self.error = Error()
        self.error.show()

    def mostrarResultado(self):
        self.resultado = Resultado()
        self.resultado.show()

    def mostrarResultadoError(self):
        self.resultadoError = resultadoError()
        self.resultadoError.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    icon = QIcon('nota.png')
    MainWindow.setWindowIcon(icon)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())