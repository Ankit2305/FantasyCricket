# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'openTeam.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_openTeamForm(object):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent

    def setupUi(self, openTeamForm):
        openTeamForm.setObjectName("openTeamForm")
        openTeamForm.resize(600, 150)
        openTeamForm.setMinimumSize(QtCore.QSize(600, 150))
        openTeamForm.setMaximumSize(QtCore.QSize(600, 150))
        self.horizontalLayout = QtWidgets.QHBoxLayout(openTeamForm)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(87, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(openTeamForm)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.teamnames = QtWidgets.QComboBox(openTeamForm)
        self.teamnames.setObjectName("teamnames")
        self.horizontalLayout.addWidget(self.teamnames)
        spacerItem1 = QtWidgets.QSpacerItem(87, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.openbutton = QtWidgets.QPushButton(openTeamForm)
        self.openbutton.setObjectName("openbutton")
        self.horizontalLayout.addWidget(self.openbutton)
        spacerItem2 = QtWidgets.QSpacerItem(87, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)

        self.retranslateUi(openTeamForm)
        QtCore.QMetaObject.connectSlotsByName(openTeamForm)

        self.fill_teamnames()
        self.openbutton.clicked.connect(self.open_team)

    def retranslateUi(self, openTeamForm):
        _translate = QtCore.QCoreApplication.translate
        openTeamForm.setWindowTitle(_translate("openTeamForm", "Open Team"))
        self.label.setText(_translate("openTeamForm", "Team Name"))
        self.openbutton.setText(_translate("openTeamForm", "Open"))

    def fill_teamnames(self):
        # fetches all the custom teams and adds them to combobox
        db = sqlite3.connect('cricket.db')
        db_cursor = db.cursor()
        db_cursor.execute('SELECT * FROM custom_teams')
        self.teams = db_cursor.fetchall()
        for team in self.teams:
            self.teamnames.addItem(team[1])
        db.close()

    def open_team(self):
        # sends team data to the mainwindow.py
        index = self.teamnames.currentIndex()
        self.parent.open_team(self.teams[index])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    openTeamForm = QtWidgets.QWidget()
    ui = Ui_openTeamForm()
    ui.setupUi(openTeamForm)
    openTeamForm.show()
    sys.exit(app.exec_())

