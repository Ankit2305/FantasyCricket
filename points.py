def compute_points(scoreboard):
	players = {}
	team1_batsmen = scoreboard[0].getbatsmen()
	team2_batsmen = scoreboard[1].getbatsmen()

	for batsman in team1_batsmen:
		points = batsman_points(batsman)
		players[batsman.id] = [batsman.name, points]

	for batsman in team2_batsmen:
		points = batsman_points(batsman)
		players[batsman.id] = [batsman.name, points]

	team1_bowlers = scoreboard[0].getbowlers()
	team2_bowlers = scoreboard[1].getbowlers()

	for bowler in team1_bowlers:
		points = bowler_points(bowler)
		player = players.get(bowler.id, [bowler.name, 0])
		player[1] += points 

	for bowler in team2_bowlers:
		points = bowler_points(bowler)
		player = players.get(bowler.id, [bowler.name, 0])
		player[1] += points 

	return players


def bowler_points(bowler):
    wickets = bowler.wicket
    economy = bowler.economy

    points = wickets * 10

    if wickets >= 3:
        points += 5
    if wickets >= 5:
        points += 10

    if 3.5 <= economy <= 4.5:
        points += 4
    if 2 <= economy <= 3.5:
        points += 7
    if economy < 2:
        points += 10

    return points


def batsman_points(batsman):
    runs = batsman.runs
    fours = batsman.fours
    sixes = batsman.sixes
    strike_rate = batsman.strike_rate

    points = runs//2

    if runs >= 50:
        points += 5
    if runs >= 100:
        points += 10

    if 80 <= strike_rate <= 100:
        points += 2
    if strike_rate > 100:
        points += 4

    points += fours + 2*sixes

    return points
