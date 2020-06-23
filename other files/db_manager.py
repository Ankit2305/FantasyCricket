import sqlite3

db = sqlite3.connect('cricket.db')
db_cursor = db.cursor()

#db_cursor.execute('CREATE TABLE playing11 (team REFERENCES teams(id), player REFERENCES players(id))')

lst = [
	'1 2 0 9 3 5 4 6 13 11 12',
	'15 16 17 19 20 22 24 25 26 27 28',
	'31 33 32 35 36 39 38 40 41 42 44',
	'45 48 49 47 50 51 52 54 55 53 57',
	'60 61 62 63 64 70 67 69 71 74 72',
	'75 76 78 83 79 77 84 80 86 87 88',
	'100 92 91 90 93 101 95 99 103 102 104',
	'105 106 112 107 113 111 110 109 117 116 114',
	'126 120 118 119 122 121 124 125 127 129 128',
	'131 132 133 134 135 140 136 137 143 144 145',
	'146 152 148 147 151 154 150 159 156 158 160',
	'167 161 162 163 164 169 168 173 174 171 170',
]

for team in range(len(lst)):
	player_ids = lst[team]
	player_list = player_ids.split(' ')
	for ids in player_list:
		id = int(ids)
		print(id, team)
		db_cursor.execute('INSERT INTO playing11 VALUES({}, {})'.format(team, id))

db.commit()
