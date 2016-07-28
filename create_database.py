import sqlite3
import os
import json


# Create pokemon database
if os.path.isfile("./pokemon.sqlite3"):
	print "Pokemon spawn database already exists.  Delete pokemon.sqlite3 if you want to regenerate it."
else:
	db = sqlite3.connect("./pokemon.sqlite3")
	c = db.cursor()
	c.execute('''create table pokemon (time INTEGER, lat REAL, lng REAL, pid INTEGER, cell TEXT, sid TEXT, CONSTRAINT unique_spawns PRIMARY KEY (time, lat, lng, pid))''')
	print "Created pokemon.sqlite3"
	if os.path.isfile("./pokes.json"):
		print "Importing spawns from pokes.json"
		with open('pokes.json') as file:
			pokes = json.load(file)
		for poke in pokes:
			try:
		                c.execute("INSERT INTO pokemon (time, lat, lng, pid, cell, sid) VALUES(?,?,?,?,?,?)",[poke['time'],poke['lat'],poke['lng'],poke['pid'],poke['cell'],poke['sid']])
		        except sqlite3.IntegrityError:
		                # Ignore errors because of duplicate records
	                	pass
	db.commit()
	db.close()
	

# Create points database
if os.path.isfile("./points.sqlite3"):
	print "Points database already exists. Delete points.sqlite3 if you want to regenerate it."
else:
	db = sqlite3.connect("./points.sqlite3")
	c = db.cursor()
	c.execute('''create table gyms (id TEXT, lat REAL, lng REAL, team INTEGER, CONSTRAINT unique_gyms PRIMARY KEY (lat,lng))''')
	c.execute('''create table stops (id TEXT, lat REAL, lng REAL, CONSTRAINT unique_stops PRIMARY KEY(lat,lng))''')
	c.execute('''create table spawnpoints (sid TEXT, time INTEGER, lat REAL, lng REAL, cell TEXT, CONSTRAINT unique_spawnpoints PRIMARY KEY(sid, lat, lng))''')
	print "Created points.sqlite3"

	if os.path.isfile("./gyms.json"):
		print "Importing gyms from gyms.json"
		with open('gyms.json') as file:
			gyms = json.load(file)
		for gym in gyms:
			try:
		                c.execute("INSERT INTO gyms (id, lat, lng, team) VALUES(?,?,?,?)",[gym['id'],gym['lat'],gym['lng'],gym['team']])
		        except sqlite3.IntegrityError:
	                	# Ignore errors because of duplicate records
	                	pass
	if os.path.isfile("./stops.json"):
		print "Importing stops from stops.json"
		with open('stops.json') as file:
			stops = json.load(file)
		for stop in stops:
			try:
				c.execute("INSERT INTO stops (id, lat, lng) VALUES(?,?,?)",[stop['id'],stop['lat'],stop['lng']])
			except sqlite3.IntegrityError:
				# Ignore errors because of duplicate records
				pass

	if os.path.isfile("./spawns.json"):
		print "Importing spawnpoints from spawns.json"
		with open('spawns.json') as file:
			spawns = json.load(file)
		for spawn in spawns:
			try:
				c.execute("INSERT INTO spawnpoints (sid, time, lat, lng, cell) VALUES(?,?,?,?,?)",[spawn['sid'],spawn['time'],spawn['lat'],spawn['lng'],spawn['cell']])
			except sqlite3.IntegrityError:
				pass
	db.commit()
	db.close()

