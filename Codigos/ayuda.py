from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Ayuda(object):
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ayuda = QtWidgets.QWidget()
    ui = Ui_Ayuda()
    ui.setupUi(Ayuda)
    Ayuda.show()
    sys.exit(app.exec())
