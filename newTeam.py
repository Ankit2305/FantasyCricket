# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newTeam.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from alert import Ui_alert
import sqlite3


class Ui_newteam(object):
    def __init__(self, parent):
        self.parent = parent

    def setupUi(self, newteam):
        newteam.setObjectName("newteam")
        newteam.resize(600, 200)
        newteam.setMinimumSize(QtCore.QSize(600, 200))
        newteam.setMaximumSize(QtCore.QSize(600, 200))
        self.verticalLayout = QtWidgets.QVBoxLayout(newteam)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.team1 = QtWidgets.QComboBox(newteam)
        self.team1.setMinimumSize(QtCore.QSize(200, 0))
        self.team1.setObjectName("team1")
        self.horizontalLayout_3.addWidget(self.team1)
        self.label_2 = QtWidgets.QLabel(newteam)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.team2 = QtWidgets.QComboBox(newteam)
        self.team2.setMinimumSize(QtCore.QSize(200, 0))
        self.team2.setObjectName("team2")
        self.horizontalLayout_3.addWidget(self.team2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(87, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.label_3 = QtWidgets.QLabel(newteam)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.teamname = QtWidgets.QLineEdit(newteam)
        self.teamname.setMinimumSize(QtCore.QSize(200, 0))
        self.teamname.setObjectName("teamname")
        self.horizontalLayout.addWidget(self.teamname)
        self.createbutton = QtWidgets.QPushButton(newteam)
        self.createbutton.setObjectName("createbutton")
        self.horizontalLayout.addWidget(self.createbutton)
        spacerItem4 = QtWidgets.QSpacerItem(87, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.label = QtWidgets.QLabel(newteam)
        self.label.setMinimumSize(QtCore.QSize(10, 0))
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)

        self.retranslateUi(newteam)
        QtCore.QMetaObject.connectSlotsByName(newteam)
        self.fetch_teams()
        self.lock = False
        self.createbutton.clicked.connect(self.createteam)
        self.team1.currentIndexChanged.connect(self.team1change_handler)
        self.team2.currentIndexChanged.connect(self.team2change_handler)

    def retranslateUi(self, newteam):
        _translate = QtCore.QCoreApplication.translate
        newteam.setWindowTitle(_translate("newteam", "New Team"))
        self.label_2.setText(_translate("newteam", "v/s"))
        self.label_3.setText(_translate("newteam", "Team Name:"))
        self.createbutton.setText(_translate("newteam", "Create"))

    def fetch_teams(self):
        # fetches teams from the database and adds them to the combo boxes
        db = sqlite3.connect('cricket.db')
        db_cursor = db.cursor()
        db_cursor.execute('SELECT * FROM teams')
        self.teams = db_cursor.fetchall()

        for i in range(len(self.teams)):
            if i == 1:
                continue
            self.team1.addItem(self.teams[i][1])

        for i in range(len(self.teams)):
            if i == 0:
                continue
            self.team2.addItem(self.teams[i][1])

        db.close()

    def team1change_handler(self):
        # on selecting an team in team1 combo box, that selected team is removed from the options in team2 combo box
        if self.lock:
            return
        self.lock = True
        team2 = self.team2.currentText()
        self.team2.clear()
        index = 0
        skip = 0
        team1 = self.team1.currentText()

        for i in range(len(self.teams)):
            if self.teams[i][1] == team1:
                skip = i
                continue
            self.team2.addItem(self.teams[i][1])
            if self.teams[i][1] == team2:
                index = i

        if index > skip:
            index -= 1
        self.team2.setCurrentIndex(index)
        self.lock = False

    def team2change_handler(self):
        # on selecting an team in team2 combo box, that selected team is removed from the options in team1 combo box
        if self.lock:
            return 
        self.lock = True
        team1 = self.team1.currentText()
        self.team1.clear()
        index = 0
        skip = 0
        team2 = self.team2.currentText()

        for i in range(len(self.teams)):
            if self.teams[i][1] == team2:
                skip = i
                continue
            self.team1.addItem(self.teams[i][1])
            if self.teams[i][1] == team1:
                index = i

        if index > skip:
            index -= 1
        self.team1.setCurrentIndex(index)
        self.lock = False

    def createteam(self):
        # sends team data to the mainwindow.py
        team_name = self.teamname.text()
        if len(team_name) == 0:
            self.alert = QtWidgets.QWidget()
            self.ui = Ui_alert(self, 'Please enter a team name')
            self.ui.setupUi(self.alert)
            self.alert.show()
        else:
            team1 = self.team1.currentText()
            team2 = self.team2.currentText()
            team1_id = 0
            team2_id = 1

            for team in self.teams:
                if team1 == team[1]:
                    team1_id = team[0]
                if team2 == team[1]:
                    team2_id = team[0]

            self.parent.createteam(team_name, team1_id, team2_id)

    def closealert(self):
        # closes alert.py window
        self.alert.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    newteam = QtWidgets.QWidget()
    ui = Ui_newteam()
    ui.setupUi(newteam)
    newteam.show()
    sys.exit(app.exec_())
