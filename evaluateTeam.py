# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evaluateTeam.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from scorecard import Ui_Form as Scorecard_Form
from points import compute_points

class Ui_evaluate_team(object):
    def __init__(self, team_name, team, scorecard, captain):
        self.scorecard = scorecard
        self.team_name = team_name
        self.team = team
        self.captain = captain

    def setupUi(self, evaluate_team):
        evaluate_team.setObjectName("evaluate_team")
        evaluate_team.resize(698, 587)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(evaluate_team)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.teamname = QtWidgets.QLabel(evaluate_team)
        self.teamname.setText("")
        self.teamname.setAlignment(QtCore.Qt.AlignCenter)
        self.teamname.setObjectName("teamname")
        self.verticalLayout_3.addWidget(self.teamname)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(evaluate_team)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.listWidget_2 = QtWidgets.QListWidget(evaluate_team)
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalLayout_2.addWidget(self.listWidget_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(evaluate_team)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listWidget = QtWidgets.QListWidget(evaluate_team)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(evaluate_team)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.pushButton = QtWidgets.QPushButton(evaluate_team)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)

        self.retranslateUi(evaluate_team)
        QtCore.QMetaObject.connectSlotsByName(evaluate_team)
        self.add_data()
        self.pushButton.clicked.connect(self.open_scorecard)

    def retranslateUi(self, evaluate_team):
        _translate = QtCore.QCoreApplication.translate
        evaluate_team.setWindowTitle(_translate("evaluate_team", "Evaluate Team"))
        self.label_2.setText(_translate("evaluate_team", "Players"))
        self.label.setText(_translate("evaluate_team", "Points"))
        self.label_3.setText(_translate("evaluate_team", "Total Points:"))
        self.pushButton.setText(_translate("evaluate_team", "View Scorecard"))

    def add_data(self):
        # adds player names and their points to the window
        self.teamname.setText(self.team_name)
        points = compute_points(self.scorecard[1])
        team_ids = self.team.split(',')
        total = 0
        for id in team_ids:
            player = points.get(int(id))


            if self.captain == int(id):
                self.listWidget_2.addItem(player[0] + ' (c)')
                self.listWidget.addItem("{}".format(2*player[1]))
                total += 2*player[1]
            else:
                self.listWidget_2.addItem(player[0])
                self.listWidget.addItem("{}".format(player[1]))
                total += player[1]


        self.label_3.setText('Total Points: {}'.format(total))


    def open_scorecard(self):
        # opens scorecard.py window
        self.Form = QtWidgets.QWidget()
        self.ui = Scorecard_Form(self.scorecard)
        self.ui.setupUi(self.Form)
        self.Form.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    evaluate_team = QtWidgets.QWidget()
    ui = Ui_evaluate_team()
    ui.setupUi(evaluate_team)
    evaluate_team.show()
    sys.exit(app.exec_())
