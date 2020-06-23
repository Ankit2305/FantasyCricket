# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alert.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_alert(object):
    def __init__(self, parent, message_text):
        self.parent = parent
        self.message_text = message_text

    def setupUi(self, alert):
        alert.setObjectName("alert")
        alert.resize(600, 200)
        alert.setMinimumSize(QtCore.QSize(600, 200))
        alert.setMaximumSize(QtCore.QSize(600, 200))
        self.verticalLayout = QtWidgets.QVBoxLayout(alert)
        self.verticalLayout.setObjectName("verticalLayout")
        self.message = QtWidgets.QLabel(alert)
        self.message.setText("")
        self.message.setAlignment(QtCore.Qt.AlignCenter)
        self.message.setObjectName("message")
        self.verticalLayout.addWidget(self.message)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.okbutton = QtWidgets.QPushButton(alert)
        self.okbutton.setObjectName("okbutton")
        self.horizontalLayout.addWidget(self.okbutton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(alert)
        QtCore.QMetaObject.connectSlotsByName(alert)
        self.message.setText(self.message_text)
        self.okbutton.clicked.connect(self.close)

    def retranslateUi(self, alert):
        _translate = QtCore.QCoreApplication.translate
        alert.setWindowTitle(_translate("alert", "Alert"))
        self.okbutton.setText(_translate("alert", "OK"))

    def close(self):
        # closes window
        self.parent.closealert()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    alert = QtWidgets.QWidget()
    ui = Ui_alert()
    ui.setupUi(alert)
    alert.show()
    sys.exit(app.exec_())
