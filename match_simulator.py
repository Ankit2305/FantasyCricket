from team import Team
from game_events import compute_ball, toss

def simulate_inning(team, target = None):
	# simulate inning of the given team
	team.start_inning()
	overs = 50

	for over in range(overs):
		ball = 1
		if over % 10 == 0:
			team.change_bowling_pair(over)
		else:
			team.change_bowler()
		team.change_strike()
		while ball <= 6:
			ball += 1
			batsman_confidence = team.getbatsmanconfidence()
			batsman_level = team.getbatsmanlevel()
			bowler_confidence = team.getbowlerconfidence()
			bowler_level = team.getbowlerlevel()
			ball_result = compute_ball(batsman_level, bowler_level, batsman_confidence, bowler_confidence)
			if ball_result < -1:
				ball -= 1
			cont = team.update_score(ball_result)

			if (target is not None and team.getscore() > target) or not cont:
				return 


def simulate_match(team1, team2):
	# simulates match for the given teams
	team = [team1, team2]

	teams = []
	teams.append(Team(team[0], team[1]))
	teams.append(Team(team[1], team[0]))

	toss_result = toss(teams[0].teamname(), teams[1].teamname())

	simulate_inning(teams[toss_result[0]])
	simulate_inning(teams[(toss_result[0] + 1) % 2], teams[toss_result[0]].getscore())
	
	return (toss_result, teams)
