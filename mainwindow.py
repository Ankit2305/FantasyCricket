# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from openTeam import Ui_openTeamForm
from evaluateTeam import Ui_evaluate_team
from alert import Ui_alert
from newTeam import Ui_newteam
from rules import Ui_rules
from match_scorecard import scorecard
import sqlite3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(695, 636)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.batcount = QtWidgets.QLabel(self.centralwidget)
        self.batcount.setObjectName("batcount")
        self.horizontalLayout_2.addWidget(self.batcount)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.ballcount = QtWidgets.QLabel(self.centralwidget)
        self.ballcount.setObjectName("ballcount")
        self.horizontalLayout_2.addWidget(self.ballcount)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.arcount = QtWidgets.QLabel(self.centralwidget)
        self.arcount.setObjectName("arcount")
        self.horizontalLayout_2.addWidget(self.arcount)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.wkcount = QtWidgets.QLabel(self.centralwidget)
        self.wkcount.setObjectName("wkcount")
        self.horizontalLayout_2.addWidget(self.wkcount)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        self.availpoint = QtWidgets.QLabel(self.centralwidget)
        self.availpoint.setObjectName("availpoint")
        self.horizontalLayout_3.addWidget(self.availpoint)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10)
        self.usedpoint = QtWidgets.QLabel(self.centralwidget)
        self.usedpoint.setObjectName("usedpoint")
        self.horizontalLayout_3.addWidget(self.usedpoint)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_5.addWidget(self.radioButton)
        self.radiobat = QtWidgets.QRadioButton(self.centralwidget)
        self.radiobat.setObjectName("radiobat")
        self.horizontalLayout_5.addWidget(self.radiobat)
        self.radiobowl = QtWidgets.QRadioButton(self.centralwidget)
        self.radiobowl.setObjectName("radiobowl")
        self.horizontalLayout_5.addWidget(self.radiobowl)
        self.radioar = QtWidgets.QRadioButton(self.centralwidget)
        self.radioar.setObjectName("radioar")
        self.horizontalLayout_5.addWidget(self.radioar)
        self.radiowk = QtWidgets.QRadioButton(self.centralwidget)
        self.radiowk.setObjectName("radiowk")
        self.horizontalLayout_5.addWidget(self.radiowk)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_4.addWidget(self.label_15)
        self.teamname = QtWidgets.QLabel(self.centralwidget)
        self.teamname.setMinimumSize(QtCore.QSize(200, 0))
        self.teamname.setText("")
        self.teamname.setObjectName("teamname")
        self.horizontalLayout_4.addWidget(self.teamname)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.unselected = QtWidgets.QListWidget(self.centralwidget)
        self.unselected.setObjectName("unselected")
        self.horizontalLayout.addWidget(self.unselected)
        self.selected = QtWidgets.QListWidget(self.centralwidget)
        self.selected.setObjectName("selected")
        self.horizontalLayout.addWidget(self.selected)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.resetbutton = QtWidgets.QPushButton(self.centralwidget)
        self.resetbutton.setObjectName("resetbutton")
        self.horizontalLayout_6.addWidget(self.resetbutton)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_6.addWidget(self.label_16)
        self.captain = QtWidgets.QComboBox(self.centralwidget)
        self.captain.setObjectName("captain")
        self.captain.setMinimumSize(QtCore.QSize(250, 0))
        self.horizontalLayout_6.addWidget(self.captain)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 695, 26))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Team = QtWidgets.QAction(MainWindow)
        self.actionNew_Team.setObjectName("actionNew_Team")
        self.actionSave_Team = QtWidgets.QAction(MainWindow)
        self.actionSave_Team.setObjectName("actionSave_Team")
        self.actionOpen_Team = QtWidgets.QAction(MainWindow)
        self.actionOpen_Team.setObjectName("actionOpen_Team")
        self.actionEvaluate_Team = QtWidgets.QAction(MainWindow)
        self.actionEvaluate_Team.setObjectName("actionEvaluate_Team")
        self.menuManage_Teams.addAction(self.actionNew_Team)
        self.menuManage_Teams.addAction(self.actionSave_Team)
        self.menuManage_Teams.addAction(self.actionOpen_Team)
        self.menuManage_Teams.addAction(self.actionEvaluate_Team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.menuManage_Teams.triggered[QtWidgets.QAction].connect(self.menufunctions)
        self.can_evaluate = False
        self.resetbutton.clicked.connect(self.reset)
        self.players = []
        self.selected.itemDoubleClicked.connect(self.remove_from_selected)
        self.unselected.itemDoubleClicked.connect(self.add_to_selected)
        self.radioButton.toggled.connect(self.all_radio)
        self.radioar.toggled.connect(self.ar_radio)
        self.radiobat.toggled.connect(self.bat_radio)
        self.radiobowl.toggled.connect(self.bowl_radio)
        self.radiowk.toggled.connect(self.wk_radio)
        self.team_name = ''
        self.unselected_players = []
        self.selected_players = []


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fantasy Cricket"))
        self.label.setText(_translate("MainWindow", "Your Selection"))
        self.label_5.setText(_translate("MainWindow", "Batsmen:"))
        self.batcount.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "Bowlers:"))
        self.ballcount.setText(_translate("MainWindow", "0"))
        self.label_7.setText(_translate("MainWindow", "Allrounders:"))
        self.arcount.setText(_translate("MainWindow", "0"))
        self.label_8.setText(_translate("MainWindow", "Wicket Keepers:"))
        self.wkcount.setText(_translate("MainWindow", "0"))
        self.label_11.setText(_translate("MainWindow", "Points Available:"))
        self.availpoint.setText(_translate("MainWindow", "1000"))
        self.label_10.setText(_translate("MainWindow", "Points Used:"))
        self.usedpoint.setText(_translate("MainWindow", "0"))
        self.radioButton.setText(_translate("MainWindow", "ALL"))
        self.radiobat.setText(_translate("MainWindow", "BAT"))
        self.radiobowl.setText(_translate("MainWindow", "BOWL"))
        self.radioar.setText(_translate("MainWindow", "AR"))
        self.radiowk.setText(_translate("MainWindow", "WK"))
        self.label_15.setText(_translate("MainWindow", "Team Name:"))
        self.resetbutton.setText(_translate("MainWindow", "Reset"))
        self.label_16.setText(_translate("MainWindow", "Captain:"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNew_Team.setText(_translate("MainWindow", "New Team"))
        self.actionSave_Team.setText(_translate("MainWindow", "Save Team"))
        self.actionOpen_Team.setText(_translate("MainWindow", "Open Team"))
        self.actionEvaluate_Team.setText(_translate("MainWindow", "Evaluate Team"))

    def menufunctions(self, action):
        # adds functionality to the menu
        text = action.text()
        if text == 'New Team':
            self.newteam = QtWidgets.QWidget()
            self.ui = Ui_newteam(self)
            self.ui.setupUi(self.newteam)
            self.newteam.show()
        elif text == 'Open Team':
            self.openTeamForm = QtWidgets.QWidget()
            self.ui = Ui_openTeamForm(self)
            self.ui.setupUi(self.openTeamForm)
            self.openTeamForm.show()
        elif text == 'Save Team':
            if len(self.team_name) > 0:
                self.save_team()
            else:
                self.user_alert('Please open or create new team to save')
        else:
            if self.can_evaluate:
                self.evaluate_team = QtWidgets.QWidget()
                self.ui = Ui_evaluate_team(self.team_name, self.team[4], scorecard(self.team[2], self.team[3]), self.captain_id())
                self.ui.setupUi(self.evaluate_team)
                self.evaluate_team.show()
            else:
                self.user_alert("Team don't have enough players")

    def closealert(self):
        # closes alert.py window
        self.alert.close()

    def createteam(self, team_name, team1_id, team2_id):
        # takes argunments from newTeam.py window and creates an empty team
        self.newteam.close()

        if self.team_exist_in_db(team_name):
            self.user_alert('Team name is already taken please use some other name')
            return

        self.team = [0, team_name, team1_id, team2_id, '']
        self.update_display()

    def open_team(self, team):
        # takes arguments from openTeam.py and opens the team 
        self.team = list(team)
        self.openTeamForm.close()
        self.update_display()

    def get_selected_players(self, team_players):
        # generates list of selected players from string of player_ids seperated by comma
        team_players_ids = team_players.split(',')
        for id in team_players_ids:
            if id == '':
                continue
            self.db_cursor.execute('SELECT * FROM players WHERE id = {}'.format(int(id)))
            self.selected_players.append(self.db_cursor.fetchall()[0])

    def count_roles(self):
        # computes the count for each role and updates that number on window
        self.batsmen = 0
        self.bowlers = 0
        self.allrounders = 0
        self.wicketkeeper = 0

        for player in self.selected_players:
            role = player[3]
            if role == 'Batsman':
                self.batsmen += 1
            elif role == 'Bowler':
                self.bowlers += 1
            elif role == 'All Rounder':
                self.allrounders += 1
            else:
                self.wicketkeeper += 1

        self.update_role_count_display()

    def update_role_count_display(self):
        # updates the count of different roles on the window
        self.batcount.setText('{}'.format(self.batsmen))
        self.ballcount.setText('{}'.format(self.bowlers))
        self.arcount.setText('{}'.format(self.allrounders))
        self.wkcount.setText('{}'.format(self.wicketkeeper))

    def update_display(self):
        # updates the window the currently open team
        self.selected.clear()
        self.unselected.clear()
        self.captain.clear()
        self.team_name = self.team[1]
        team1_id = self.team[2]
        team2_id = self.team[3]
        team_players = self.team[4]

        self.teamname.setText(self.team_name)
        self.db = sqlite3.connect('cricket.db')
        self.db_cursor = self.db.cursor()

        self.db_cursor.execute('SELECT players.* FROM players, playing11 WHERE (playing11.team = {} or playing11.team = {}) and players.id = playing11.player'.format(team1_id, team2_id))
        self.players = self.db_cursor.fetchall()

        self.selected_players = []
        self.get_selected_players(team_players)

        self.db.close()
        
        self.unselected_players = []
        for player in self.players:
            if player in self.selected_players:
                continue
            self.unselected_players.append(player)

        self.all_radio()
        self.radioButton.setChecked(True)

        for player in self.selected_players:
            self.captain.addItem(player[1])

        for i in range(len(self.selected_players)):
            if self.selected_players[i][0] == self.team[5]:
                self.captain.setCurrentIndex(i)
                break

        if len(self.selected_players) == 11:
            self.can_evaluate = True

        self.count_roles()
        self.points_available()


    def reset(self):
        # resets the selected players to empty list and reflects the changes in window
        self.selected.clear()
        self.unselected.clear()
        self.captain.clear()
        self.can_evaluate = False
        self.selected_players = []
        self.unselected_players = []
        self.team[4] = ''

        for player in self.players:
            self.unselected_players.append(player)

        self.count_roles()
        self.points_available()
        self.all_radio()
        self.radioButton.setChecked(True)

    def add_to_selected(self, item):
        # adds player from unselected players to selected players on double clicking
        if len(self.selected_players) == 11:
            self.user_alert('Cannot select more than 11 players')
            return 

        name = item.text()
        index = 0

        for i in range(len(self.unselected_players)):
            player = self.unselected_players[i]
            if player[1] == name:
                index = i
                break

        role = self.unselected_players[index][3]

        if self.check(role):
            return 

        self.unselected.takeItem(self.unselected.row(item))
        self.selected.addItem(item.text())
        self.captain.addItem(item.text())

        for player in self.players:
            if item.text() == player[1]:
                self.selected_players.append(player)
                self.unselected_players.pop(index)
                break
        
        if len(self.selected_players) == 11:
            self.can_evaluate = True
            self.collect_player_ids()

        self.count_roles()
        self.points_available()

    def collect_player_ids(self):
        # collects ids of currently selected players
        self.team[4] = ''
        for player in self.selected_players:
            self.team[4] += '{},'.format(player[0])
        self.team[4] = self.team[4][:len(self.team[4])-1]

    def remove_from_selected(self, item):
        # removes player from seleted players and moves it back to unselected players on double clicking on it
        name = item.text()
        index = 0

        for i in range(len(self.selected_players)):
            player = self.selected_players[i]
            if player[1] == name:
                index = i
                break

        self.selected.takeItem(self.selected.row(item))
        self.unselected.addItem(item.text())
        self.captain.removeItem(self.captain.findText(item.text()))

        for player in self.players:
            if item.text() == player[1]:
                self.unselected_players.append(player)
                self.selected_players.pop(index)
                break

        if len(self.selected_players) < 11:
            self.can_evaluate = False

        self.count_roles()
        self.points_available()

    def points_available(self):
        # computes the points available and points used and reflects the same on the window
        self.points = 1000 - 90 * self.batsmen - 90 * self.bowlers - 95 * self.allrounders - 90 * self.wicketkeeper
        self.usedpoint.setText('{}'.format(1000 - self.points))
        self.availpoint.setText('{}'.format(self.points))


    def all_radio(self):
        # shows all players available in selected list and unselected list
        self.selected.clear()
        self.unselected.clear()

        for player in self.unselected_players:
            self.unselected.addItem(player[1])

        for player in self.selected_players:
            self.selected.addItem(player[1])

    def bat_radio(self):
        # shows only batsmen available in selected list and unselected list
        self.selected.clear()
        self.unselected.clear()

        for player in self.unselected_players:
            if player[3] == 'Batsman':
                self.unselected.addItem(player[1])

        for player in self.selected_players:
            if player[3] == 'Batsman':
                self.selected.addItem(player[1])


    def bowl_radio(self):
        # shows only bowlers available in selected list and unselected list
        self.selected.clear()
        self.unselected.clear()

        for player in self.unselected_players:
            if player[3] == 'Bowler':
                self.unselected.addItem(player[1])

        for player in self.selected_players:
            if player[3] == 'Bowler':
                self.selected.addItem(player[1])

    def ar_radio(self):
        # shows only all rounders available in selected list and unselected list
        self.selected.clear()
        self.unselected.clear()

        for player in self.unselected_players:
            if player[3] == 'All Rounder':
                self.unselected.addItem(player[1])

        for player in self.selected_players:
            if player[3] == 'All Rounder':
                self.selected.addItem(player[1])

    def wk_radio(self):
        # shows only wicket keepers available in selected list and unselected list
        self.selected.clear()
        self.unselected.clear()

        for player in self.unselected_players:
            if player[3] == 'Wicket Keeper':
                self.unselected.addItem(player[1])

        for player in self.selected_players:
            if player[3] == 'Wicket Keeper':
                self.selected.addItem(player[1])

    def check(self, role):
        # checks if all rules are being followed while adding player to the selected player list
        count = len(self.selected_players) + 1
        batsmen = self.batsmen
        bowlers = self.bowlers
        allrounders = self.allrounders
        wicketkeeper = self.wicketkeeper
        points = self.points

        if role == 'Batsman':
            batsmen += 1
            points -= 90
        elif role == 'Bowler':
            bowlers += 1
            points -= 90
        elif role == 'All Rounder':
            allrounders += 1
            points -= 95
        else:
            wicketkeeper += 1
            points -= 90

        if points < 0:
            self.user_alert("You don't have enough points.\n\nNote: Batsmen, Bowlers and Wicket-Keeper cost 90 points and\nAll-Rounders cost 95 points")
            return True

        wicketkeeper_needed = 1 - wicketkeeper

        if wicketkeeper > 1:
            self.user_alert('Your team should have 1 Wicket Keeper')
            return True

        batsmen_needed = 5 - batsmen - allrounders
        if 11 - count < batsmen_needed:
            self.user_alert('Your team should have atleast 5 Batsmen + All-Rounders')
            return True

        bowlers_needed = 5 - bowlers - allrounders
        if 11 - count < bowlers_needed:
            self.user_alert('Your team should have atleast 5 Bowlers + All-Rounders')
            return True

        if max(batsmen_needed, 0) + max(bowlers_needed, 0) + wicketkeeper_needed > 11 - count:
            self.user_alert('Your team should have 1 Wicket Keeper')
            return True

        return False

    def user_alert(self, message):
        # opens the alert.py window with message in it
        self.alert = QtWidgets.QWidget()
        self.ui = Ui_alert(self, message)
        self.ui.setupUi(self.alert)
        self.alert.show()

    def save_team(self):
        # saves currently open team into the database
        captain_id = self.captain_id()
        self.collect_player_ids()

        db = sqlite3.connect('cricket.db')
        db_cursor = db.cursor()

        if self.team_exist_in_db(self.team_name):
            try:
                db_cursor.execute('UPDATE custom_teams SET players = "{}", captain = {} where name = "{}"'.format(self.team[4], captain_id, self.team[1]))
                
                db.commit()
                self.user_alert('{} saved successfully'.format(self.team_name))
            except:
                db.rollback()
                self.user_alert('Some error occured while saving team')

        else:
            try:
                db_cursor.execute('INSERT INTO custom_teams VALUES(0, "{}", {}, {}, "{}", {})'.format(self.team[1], self.team[2], self.team[3], self.team[4], captain_id))
                db.commit()
                self.user_alert('{} saved successfully'.format(self.team_name))
            except:
                db.rollback()
                self.user_alert('Some error occured while saving team')

    def team_exist_in_db(self, team_name):
        # checks if there exists a team with the given name in database
        db = sqlite3.connect('cricket.db')
        db_cursor = db.cursor()

        db_cursor.execute('SELECT * FROM custom_teams WHERE name = "{}"'.format(team_name))
        team = db_cursor.fetchall()

        db.close()

        return len(team) > 0

    def captain_id(self):
        # return the id of the captain
        captain_id = -1

        for player in self.players:
            if player[1] == self.captain.currentText():
                captain_id = player[0]

        return captain_id

    def open_rules(self):
        # opens the rules.py window
        self.rules = QtWidgets.QWidget()
        self.ui = Ui_rules(self)
        self.ui.setupUi(self.rules)
        self.rules.show()

    def close_rules(self):
        # closes the rules.py window
        self.rules.close()
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.open_rules()
    sys.exit(app.exec_())
