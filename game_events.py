import random

def toss(team1, team2):
	# computes toss result and decision made by toss winner
	toss_result = random.randrange(0, 2)
	toss_winning_team = team2
	if toss_result == 0:
		toss_winning_team = team1

	decide = random.randrange(0, 2)
	decision = 'Bat'
	if decide == 0:
		decision = 'Bowl'

	first_inning_batting = 0
	if (toss_result == 0 and decide == 0) or (toss_result == 1 and decide == 1):
		first_inning_batting = 1

	return (first_inning_batting, '{} has won the toss and decided to {} first.'.format(toss_winning_team, decision))


def compute_probability_distribution(batsman_level, bowler_level, batsman_confidence, bowler_confidence):
	# returns probability distribution for possible events on the ball according to the batsman and bowler 
	wicket = 3
	six = 4
	four = 15
	dot = 50
	
	if batsman_confidence > 100:
		batsman_confidence = 100 - batsman_confidence
		bowler_confidence = 0

	extras = 6 - bowler_level
	six += batsman_level - bowler_level
	four += batsman_level - bowler_level
	dot -= 2*(batsman_level - bowler_level)

	confidence_factor = (batsman_confidence - bowler_confidence) // 20
	six += confidence_factor
	four += confidence_factor
	dot -= 2*confidence_factor

	base = [extras, extras+wicket, extras+wicket+six, extras+wicket+six+four, extras+wicket+six+four+dot]
	return tuple(base)

def compute_ball(batsman_level = 3, bowler_level = 3, batsman_confidence = 30, bowler_confidence = 30):
	# computes and returns event on a ball
	probabily_distribution = compute_probability_distribution(batsman_level, bowler_level, batsman_confidence, bowler_confidence)
	ball_result = random.randrange(1, 101)
	if ball_result <= probabily_distribution[0]:
		extra_type = random.randrange(1, 101)
		if extra_type <= 10:
			return -3
		else: 
			return -2
	elif ball_result <= probabily_distribution[1]:
		return -1
	elif ball_result <= probabily_distribution[2]:
		return 6
	elif ball_result <= probabily_distribution[3]:
		return 4
	elif ball_result <= probabily_distribution[4]:
		return 0
	else:
		run_prob = random.randrange(1, 101)
		if run_prob <= 60:
			return 1
		elif run_prob <= 90:
			return 2
		return 3