from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import sqlite3

def parse_url(url):
	req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	try:
		handle = urlopen(req)
		data = handle.read().decode()
		return data
	except:
		return ''


teams_url = 'https://www.cricbuzz.com/cricket-team'
teams_html = parse_url(teams_url)

team_soup = BeautifulSoup(teams_html, 'html.parser')
team_html_anchor_tags = team_soup('a')

team_links = []

print('Finding Teams...')
for anchor_tag in team_html_anchor_tags:
	link = anchor_tag.get('href', None)
	if link is not None and 'domestic' in link:
		break
	if link is not None and link.startswith('/cricket-team/'):
		team_links.append('https://www.cricbuzz.com' + link + '/players')


print('Teams found: {}'.format(len(team_links)))

print('Finding Players...')
player_links = []
players = []
for team_link in team_links:
	try:
		html = parse_url(team_link)
	except:
		continue
	soup = BeautifulSoup(html, 'html.parser')
	anchor_tags = soup('a')

	for anchor_tag in anchor_tags:
		link = anchor_tag.get('href', None)
		if link is not None and link.startswith('/profiles/'):
			player_links.append('https://www.cricbuzz.com' + link)


print('Players found: {}'.format(len(player_links)))

print('Fetching Players Data...')
for link in player_links:
	player_html = parse_url(link)
	soup = BeautifulSoup(player_html, 'html.parser')
	h1 = soup('h1')
	player = {}
	if len(h1) > 0:
		player_name = h1[0].string
		player['name'] = player_name
	div = soup('div')
	pick_role = False
	for d in div:
		if pick_role:
			player_role = d.string
			if 'A' in player_role:
				player_role = 'All Rounder'
			if 'W' in player_role:
				player_role = 'Wicket Keeper'
			player['role'] = player_role.strip()
			break
		if d.string is not None and 'Role' in d.string:
			pick_role = True
	h3 = soup('h3')
	if len(h3) > 0:
		player['country'] = h3[0].string
	if len(player) == 3:
		players.append(player)
		print(player)

print('inserting Players into DB...')
db = sqlite3.connect('fantasy_cricket.db')
db_cursor = db.cursor()

try:
	db.execute('CREATE TABLE players (name, country, role)')
	print('Database created ...')
except:
	print('Database found...')

for player in players:
	try:
		db.execute('INSERT INTO players VALUES("{}", "{}", "{}")'.format(player['name'], player['country'], player['role']))
	except:
		print('Error while inserting player in db')
		db.rollback()
		quit()

db.commit()
