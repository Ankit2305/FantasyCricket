# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rules.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_rules(object):
    def __init__(self, parent):
        self.parent = parent

    def setupUi(self, rules):
        rules.setObjectName("rules")
        rules.resize(700, 635)
        rules.setMinimumSize(QtCore.QSize(700, 600))
        rules.setMaximumSize(QtCore.QSize(700, 701))
        self.verticalLayout = QtWidgets.QVBoxLayout(rules)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(rules)
        self.label_3.setMinimumSize(QtCore.QSize(300, 300))
        self.label_3.setMaximumSize(QtCore.QSize(300, 300))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("logos/Fantasy Cricket.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_4 = QtWidgets.QLabel(rules)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label = QtWidgets.QLabel(rules)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(rules)
        self.label_2.setMaximumSize(QtCore.QSize(60000, 16777215))
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(rules)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(rules)
        QtCore.QMetaObject.connectSlotsByName(rules)
        self.pushButton.clicked.connect(self.close)

    def retranslateUi(self, rules):
        _translate = QtCore.QCoreApplication.translate
        rules.setWindowTitle(_translate("rules", "Welcome to Fantasy Cricket"))
        self.label_4.setText(_translate("rules", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ef2929;\">Welcome to Fantasy Cricket</span></p></body></html>"))
        self.label.setText(_translate("rules", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Rules</span></p></body></html>"))
        self.label_2.setText(_translate("rules", "<html><head/><body>\n"
"<ol>\n"
"<li>Your team should have atleast 5 Batsmen + All Rounders.</li><li>Your team should have atleast 5 Bowlers + All Rounders.</li><li>Your team can only have 1 Wicket Keeper.</li><li>You are given 1000 points to create your team, all Batsmen, Bowlers and <br>Wicket Keeper cost 90 points and All Rounders cost 95 points</li><li>Select a Captain for your team. Captain\'s point are multiplied by 2 <br>while evaluating team.</li>\n"
"</ol>\n"
"</body></html>"))
        self.pushButton.setText(_translate("rules", "Close"))

    def close(self):
        self.parent.close_rules()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    rules = QtWidgets.QWidget()
    ui = Ui_rules()
    ui.setupUi(rules)
    rules.show()
    sys.exit(app.exec_())
