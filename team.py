from batsman import Batsman
from bowler import Bowler

class Team:
	def __init__(self, team, bowling_team):
		self.batsmen = []
		for player in team['players']:
			self.batsmen.append(Batsman(player))
		self.bowler = []
		bowling_team['players'].reverse()
		for player in bowling_team['players']:
			if player['role'] == 'Bowler':
				self.bowler.append(Bowler(player))
			if len(self.bowler) == 6:
				break

		for player in bowling_team['players']:
			if player['role'] == 'All Rounder':
				self.bowler.append(Bowler(player))
			if len(self.bowler) == 6:
				break
		bowling_team['players'].reverse()

		self.name = team['name']
		self.opponent_name = bowling_team['name']
		self.onstrike_batsman = 0
		self.offstrike_batsman = 1
		self.score = 0
		self.wickets = 0
		self.run_rate = 0
		self.balls = 0
		self.sixes = 0
		self.fours = 0
		self.extras = 0
		self.current_bowler = 0
		self.bowling_pair = (0,1)
		self.bowler_index = 0


	def next_batsman(self):
		# determines next available batsman on wicket
		return max([self.onstrike_batsman, self.offstrike_batsman]) + 1

	def change_bowling_pair(self, over):
		# changes bowling pair 
		over //= 10
		pair = ((0,1), (2,3), (4,2), (4,3), (1,0))
		self.bowling_pair = pair[over]
		self.bowler_index = 0
		self.current_bowler = self.bowling_pair[self.bowler_index]

	def change_bowler(self):
		# changes bowler out of selected bowing pair
		self.bowler_index = (self.bowler_index + 1)%2
		self.current_bowler = self.bowling_pair[self.bowler_index]

	def wicket(self):
		# sets onstrike batsman to out and sends next batsman
		self.batsmen[self.onstrike_batsman].out()
		self.onstrike_batsman = self.next_batsman()
		self.wickets += 1

		# If all 10 batsman are out then return False to stop the innings
		if self.onstrike_batsman > 10:
			return False

		self.batsmen[self.onstrike_batsman].send()
		return True

	def change_strike(self):
		# changes strike of onstrike and offstrike batsman
		temp = self.onstrike_batsman
		self.onstrike_batsman = self.offstrike_batsman
		self.offstrike_batsman = temp

	def update_score(self, run):
		# update the team and batsman score according to the given event on the ball
		cont = True

		self.batsmen[self.onstrike_batsman].update_score(run)
		self.bowler[self.current_bowler].update_score(run)

		if run >= 0:
			self.balls += 1
			self.score += run

		if run == 6:
			self.sixes += 1
		elif run == 4:
			self.fours += 1
		elif run < -1:
			self.score += 1
			self.extras += 1
		elif run == -1:
			self.balls += 1
			cont = self.wicket()

		if self.balls > 0:
			self.run_rate = round(6 * self.score / self.balls, 2)

		if run > 0 and run % 2 == 1:
			self.change_strike()

		return cont

	def overs(self):
		# returns the number of overs played by the team
		over = self.balls // 6
		ball = self.balls % 6
		ball /= 10
		return over + ball

	def print_scorecard(self):
		# prints scorecard on the console [ for debugging ]
		print('\nBatting Stats : ' + self.name)
		for player in self.batsmen:
			player.print_batsman()
		print('\nBowling Stats : ' + self.opponent_name)
		for bowler in self.bowler:
			bowler.print_bowler()
		print('')
		print('{}: {}/{} in {} overs\t\t| Extras: {} \t\t| Run Rate: {}'.format(self.name, self.score, self.wickets, self.overs(), self.extras, self.run_rate))
		print('---------------------------------------------------------------------------------\n')

	def start_inning(self):
		# sends first two batsman to start the inning
		self.batsmen[self.onstrike_batsman].send()
		self.batsmen[self.offstrike_batsman].send()

	def teamname(self):
		# return the name of the team
		return self.name

	def getscore(self):
		# returns the score of the team
		return self.score

	def getbatsmanlevel(self):
		# returns the level of onstrike batsman
		return self.batsmen[self.onstrike_batsman].level()

	def getbatsmanconfidence(self):
		# returns the confidence of onstrike batsman
		return self.batsmen[self.onstrike_batsman].confidence()

	def getbowlerlevel(self):
		# returns the level of current bowler
		return self.bowler[self.bowler_index].level()

	def getbowlerconfidence(self):
		# returrns confidence of current bowler
		return self.bowler[self.bowler_index].confidence()

	def getbatsmen(self):
		# returns list of all batsmen
		return self.batsmen

	def getbowlers(self):
		# return list of all bowlers
		return self.bowler
