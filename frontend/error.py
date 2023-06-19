from PyQt6 import QtCore, QtGui, QtWidgets


class Error(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(200, 100)
        Form.setMinimumSize(QtCore.QSize(200, 100))
        Form.setMaximumSize(QtCore.QSize(200, 100))
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(10, 5, 181, 61))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(60, 70, 75, 24))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Error"))
        self.label.setText(_translate("Form", "Ingresa una palabra o un valor."))
        self.pushButton.setText(_translate("Form", "Aceptar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Error()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
