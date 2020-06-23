from match_simulator import simulate_match
import sqlite3

def scorecard(team1_id, team2_id):
	# fetches team data from database and simulates match and returns scorecard
	db = sqlite3.connect('cricket.db')
	db_cursor = db.cursor()

	db_cursor.execute('SELECT name FROM teams WHERE id = {}'.format(team1_id))
	team1_name = db_cursor.fetchall()[0][0]

	db_cursor.execute('SELECT name FROM teams WHERE id = {}'.format(team2_id))
	team2_name = db_cursor.fetchall()[0][0]

	db_cursor.execute('SELECT players.* FROM players, playing11 WHERE playing11.team = {} and playing11.player = players.id'.format(team1_id))

	team1_players = db_cursor.fetchall()

	selected = []

	for player in team1_players:
		selected.append({ 'id': player[0], 'name':player[1], 'role':player[3] })

	team1 = {'name': team1_name, 'players': selected}

	db_cursor.execute('SELECT players.* FROM players, playing11 WHERE playing11.team = {} and playing11.player = players.id'.format(team2_id))

	team2_players = db_cursor.fetchall()
	selected = []

	for player in team2_players:
		selected.append({ 'id': player[0], 'name':player[1], 'role':player[3] })

	team2 = {'name': team2_name, 'players': selected}

	db.close()
	return simulate_match(team1, team2)
