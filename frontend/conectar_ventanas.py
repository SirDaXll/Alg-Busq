import sys
import pandas as pd
from PyQt6 import QtCore, QtGui, QtWidgets

class Ayuda(QtWidgets.QWidget):
    def setupUi(self, Ayuda):
        Ayuda.setObjectName("Ayuda")
        Ayuda.resize(400, 400)
        Ayuda.setMinimumSize(QtCore.QSize(400, 400))
        Ayuda.setMaximumSize(QtCore.QSize(400, 400))
        self.siguiente = QtWidgets.QPushButton(parent=Ayuda)
        self.siguiente.setGeometry(QtCore.QRect(320, 370, 75, 24))
        self.siguiente.setObjectName("siguiente")
        self.label = QtWidgets.QLabel(parent=Ayuda)
        self.label.setGeometry(QtCore.QRect(10, 0, 381, 361))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.atras = QtWidgets.QPushButton(parent=Ayuda)
        self.atras.setGeometry(QtCore.QRect(10, 370, 75, 24))
        self.atras.setObjectName("atras")

        self.retranslateUi(Ayuda)
        QtCore.QMetaObject.connectSlotsByName(Ayuda)

    def retranslateUi(self, Ayuda):
        _translate = QtCore.QCoreApplication.translate
        Ayuda.setWindowTitle(_translate("Ayuda", "Ayuda"))
        self.siguiente.setText(_translate("Ayuda", "Siguiente"))
        self.label.setText(_translate("Ayuda", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">Documentación/Manual<br/>del usuario</span></p></body></html>"))
        self.atras.setText(_translate("Ayuda", "Atrás"))


class Error(QtWidgets.QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(200, 100)
        Form.setMinimumSize(QtCore.QSize(200, 100))
        Form.setMaximumSize(QtCore.QSize(200, 100))
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(10, 5, 181, 61))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.aceptar = QtWidgets.QPushButton(parent=Form)
        self.aceptar.setGeometry(QtCore.QRect(70, 70, 75, 24))
        self.aceptar.setObjectName("aceptar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Error"))
        self.label.setText(_translate("Form", "¡Ha ocurrido un error!"))
        self.aceptar.setText(_translate("Form", "Aceptar"))


class Resultado(QtWidgets.QWidget):
    def setupUi(self, Resultado):
        Resultado.setObjectName("Resultado")
        Resultado.resize(400, 400)
        Resultado.setMinimumSize(QtCore.QSize(400, 400))
        Resultado.setMaximumSize(QtCore.QSize(400, 400))
        self.label = QtWidgets.QLabel(parent=Resultado)
        self.label.setGeometry(QtCore.QRect(10, 0, 381, 361))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.siguiente = QtWidgets.QPushButton(parent=Resultado)
        self.siguiente.setGeometry(QtCore.QRect(320, 370, 75, 24))
        self.siguiente.setObjectName("siguiente")
        self.atras = QtWidgets.QPushButton(parent=Resultado)
        self.atras.setGeometry(QtCore.QRect(10, 370, 75, 24))
        self.atras.setObjectName("atras")

        self.retranslateUi(Resultado)
        QtCore.QMetaObject.connectSlotsByName(Resultado)

    def retranslateUi(self, Resultado):
        _translate = QtCore.QCoreApplication.translate
        Resultado.setWindowTitle(_translate("Resultado", "Resultado"))
        self.label.setText(_translate("Resultado", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">Resultado</span></p></body></html>"))
        self.siguiente.setText(_translate("Resultado", "Siguiente"))
        self.atras.setText(_translate("Resultado", "Atrás"))

class Ui_MainWindow(QtWidgets.QMainWindow):
    mostrarVentanaAyuda = QtCore.pyqtSignal()
    mostrarVentanaError = QtCore.pyqtSignal()
    mostrarVentanaResultado = QtCore.pyqtSignal()

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
        self.comboBox.setGeometry(QtCore.QRect(120, 100, 160, 24))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.botonAyuda = QtWidgets.QPushButton(parent=self.centralwidget)
        self.botonAyuda.setGeometry(QtCore.QRect(10, 370, 75, 24))
        self.botonAyuda.setObjectName("botonAyuda")
        self.botonCalcular = QtWidgets.QPushButton(parent=self.centralwidget)
        self.botonCalcular.setGeometry(QtCore.QRect(320, 370, 75, 24))
        self.botonCalcular.setObjectName("botonCalcular")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Título de la ventana principal</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Descripción de la ventana principal</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Opción 1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Opción 2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Opción 3"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Opción 4"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Opción 5"))
        self.botonAyuda.setText(_translate("MainWindow", "Ayuda"))
        self.botonCalcular.setText(_translate("MainWindow", "Calcular"))

    def mostrarAyuda(self):
        self.hide()
        ventanaAyuda = Ayuda()
        ventanaAyuda.setupUi(ventanaAyuda)
        ventanaAyuda.show()

    def mostrarError(self):
        self.hide()
        ventanaError = Error()
        ventanaError.setupUi(ventanaError)
        ventanaError.show()

    def mostrarResultado(self):
        self.hide()
        ventanaResultado = Resultado()
        ventanaResultado.setupUi(ventanaResultado)
        ventanaResultado.show()

    def cargarDatos(self):
        dataset_path = "dataset/anime.csv"
        try:
            dataframe = pd.read_csv(dataset_path)

            num_rows, num_cols = dataframe.shape
   
            self.tabla.setColumnCount(num_cols)
            self.tabla.setRowCount(num_rows)

            column_labels = dataframe.columns.tolist()
            self.tabla.setHorizontalHeaderLabels(column_labels)

            for i in range(num_rows):
                row_data = dataframe.iloc[i].tolist()
                for j in range(num_cols):
                    item = QtWidgets.QTableWidgetItem(str(row_data[j]))
                    self.tabla.setItem(i, j, item)

            self.mostrarVentanaResultado.emit()
        except:
            self.mostrarVentanaError.emit()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    ui.mostrarVentanaAyuda.connect(ui.mostrarAyuda)
    ui.mostrarVentanaError.connect(ui.mostrarError)
    ui.mostrarVentanaResultado.connect(ui.mostrarResultado)

    sys.exit(app.exec())
