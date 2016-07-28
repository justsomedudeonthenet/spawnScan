import json
import sqlite3

db = sqlite3.connect("pokemon.sqlite3")
c = db.cursor()

with open('pokes.json') as file:
	pokes = json.load(file)

for poke in pokes:
	try:
		c.execute("INSERT INTO pokemon (time, lat, lng, pid, cell, sid) VALUES(?,?,?,?,?,?)",[poke['time'],poke['lat'],poke['lng'],poke['pid'],poke['cell'],poke['sid']])
	except sqlite3.IntegrityError:
		# Ignore errors because of duplicate records
		print "Duplicate spawn not added."
		pass
db.commit()
db.close()
