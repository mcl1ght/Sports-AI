# Import the machine learning "classifier" we want to test.
from sklearn.ensemble import RandomForestClassifier
# Import the numpy package with "np" as an alias.
import numpy as np
import csv

# Create an "classifier" object which will try to "learn" our function
clf = RandomForestClassifier()

playerRoster = []

class Player:
	def __init__(self, name, rating, team, position):
		self.name = name
		self.rating = rating
		self.team = team
		self.position = position

rows = []

with open('NBA-Stats-2021-22.csv', newline='') as csvfile:
	# creating a csv reader object
	csvreader = csv.reader(csvfile)
      
	# extracting field names through first row
	fields = next(csvreader)
  
	# extracting each data row one by one
	for row in csvreader:
		rows.append(row)
  
	# get total number of rows
	print("Total no. of players: %d"%(csvreader.line_num))
  
# printing the field names
# FULL NAME, TEAM, POS, AGE, GP, MPG, FTA, FT%, 2PA, 2P%, 3PA, 3P%, eFG%, TS%, PPG, RPG, APG, SPG, BPG, TOPG, VI, ORTG, DRTG
print('Field names are:' + ', '.join(field for field in fields))

team = input("What team do you wan't to improve? ")

#  printing first 5 rows

for row in rows:
	if row[1] == team:
		playerRoster.append( Player(row[0],row[21],row[1],row[2]) )

for players in playerRoster:
	print(players.name)
