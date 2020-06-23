class Bowler:
	def __init__(self, bowler):
		self.name = bowler['name']
		self.role = bowler['role']
		self.id = bowler['id']
		self.runs = 0
		self.balls = 0
		self.wicket = 0
		self.economy = 0

	def update_score(self, run):
		# updates bowler stats based on the ball event
		if run >= 0:
			self.balls += 1
			self.runs += run

		if run == -1:
			self.wicket += 1
			self.balls += 1

		elif run < -1:
			self.runs += 1

		if self.balls > 0:
			self.economy = round(6*self.runs/self.balls, 2)

	def overs(self):
		# returns number of overs done by bowler
		over = self.balls // 6
		ball = self.balls % 6
		ball /= 10
		return over + ball

	def print_bowler(self):
		# prints bowler to the console [ for debugging purpose ]
		if self.balls > 0:
			print('{:30}: {}\t\t{}\t\t{}\t\t{}'.format(self.name, self.runs, self.overs(), self.wicket, self.economy))

	def level(self):
		# return level of the bowler
		if self.role == 'Batsman':
			return 2
		elif self.role == 'All Rounder':
			return 3
		elif self.role == 'Wicket Keeper':
			return 1
		else:
			return 5

	def confidence(self):
		# returns confidence of the bowler
		return self.balls



