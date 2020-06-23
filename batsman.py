class Batsman:
	def __init__(self, batsman):
		self.name = batsman['name']
		self.role = batsman['role']
		self.id = batsman['id']
		self.batted = False
		self.notout = True
		self.runs = 0
		self.fours = 0
		self.sixes = 0
		self.balls = 0
		self.strike_rate = 0

	def send(self):
		# sets batted to true 
		self.batted = True

	def asterisk(self):
		# return asterisk if batsman is notout
		if self.notout:
			return '*'
		return ''

	def update_score(self, run):
		# update batsman stats based on ball_event
		if run >= 0:
			self.balls += 1
			self.runs += run
		if run == 6:
			self.sixes += 1
		elif run == 4:
			self.fours += 1

		if run == -1:
			self.balls += 1
			self.out()

		if self.balls > 0:
			self.strike_rate = round(100 * self.runs / self.balls, 2)

	def print_batsman(self):
		# prints batsman on console [for debugging purpose]
		if self.batted:
			print('{:30}: {}{}\t\t{}\t\t{}\t\t{}\t\t{}'.format(self.name, self.runs, self.asterisk(), self.balls, self.sixes, self.fours, self.strike_rate))
		else:
			print('{:30}: Not Batted'.format(self.name))

	def out(self):
		# sets notout to false
		self.notout = False

	def level(self):
		# returns level of batsman
		if self.role == 'Batsman':
			return 5
		elif self.role == 'All Rounder':
			return 3
		elif self.role == 'Wicket Keeper':
			return 2
		else:
			return 1

	def confidence(self):
		# returns confidence of batsman
		return self.balls


