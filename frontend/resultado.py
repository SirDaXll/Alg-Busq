from PyQt6 import QtCore, QtGui, QtWidgets


class Resultado(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 400)
        Form.setMinimumSize(QtCore.QSize(400, 400))
        Form.setMaximumSize(QtCore.QSize(800, 400))
        Form.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Spanish, QtCore.QLocale.Country.Chile))
        self.tableWidget = QtWidgets.QTableWidget(parent=Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 380, 350))
        self.tableWidget.setMinimumSize(QtCore.QSize(380, 350))
        self.tableWidget.setMaximumSize(QtCore.QSize(800, 350))
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 370, 75, 24))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Resultado - Algoritmo Utilizado"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Anime"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Género"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Tipo"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Episodios"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Puntuación"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Miembros"))
        self.pushButton.setText(_translate("Form", "Cerrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Resultado()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())