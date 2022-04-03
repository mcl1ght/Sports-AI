# Import the machine learning "classifier" we want to test.
from decimal import Decimal
from tokenize import Double
from sklearn.ensemble import RandomForestClassifier
# Import the numpy package with "np" as an alias.
import numpy as np
import csv

# Create an "classifier" object which will try to "learn" our function
clf = RandomForestClassifier()

playerRoster = []
rankedRoster = []

class Player:
	def __init__(self, NAME, TEAM, POS, AGE, GP, MPG, FTA, FTP, TWPA, TWPP, THPA, THPP, eFG, TS, PPG, RPG, APG, SPG, BPG, TOPG, VI, ORTG, DRTG):
		self.name = NAME
		self.team = TEAM
		self.position = POS
		self.age = AGE
		self.gamesPlayed = GP
		self.minPerGame = MPG
		self.freeThrowsAtt = FTA
		self.freeThrowPer = FTP
		self.twoPointAtt = TWPA
		self.twoPointPer = TWPP
		self.threePointAtt = THPA
		self.threePointPer = THPP
		self.fieldGoalEff = eFG
		self.trueShooting = TS
		self.pointsPerGame = PPG
		self.reboundsPerGame = RPG
		self.assistsPerGame = APG
		self.stealsPerGame = SPG
		self.blocksPerGame = BPG
		self.turnoversPerGame = TOPG
		self.versatilityIndex = VI
		self.offensiveRating = ORTG
		self.defensiveRating = DRTG

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

guardExPlayer = ["Stephen Curry", "Kyrie Irving", "Zach LaVine", "De'Aaron Fox", "Russell Westbrook", "Pat Connaughton", "Markus Howard"]
guardExRtg = [96, 91, 88, 84, 78, 73, 67]

forwardExPlayer = ["Giannis Antetokounmpo", "Jayson Tatum", "Domantas Sabonis", "Miles Bridges", "Kelly Oubre Jr.", "Justin Holiday", "CJ Elleby"]
forwardExRtg = [96, 90, 87, 84, 78, 73, 68]

centerExPlayer = ["Nikola Jokic", "Karl-Anthony Towns", "Deandre Ayton", "Steven Adams", "DeMarcus Cousins", "Kai Jones", "Tacko Fall"]
centerExRtg = [95, 89, 86, 83, 78, 72, 71]

allPlayerRtg = []
allExStats = []

tempList = []

for row in rows:
	for index, g in enumerate(guardExPlayer):
		if g == row[0]:
			tempList.append(float(row[7]))
			tempList.append(float(row[9]))
			tempList.append(float(row[11]))
			tempList.append(float(row[14]))
			tempList.append(float(row[15]))
			tempList.append(float(row[16]))
			tempList.append(float(row[17]))
			tempList.append(float(row[18]))
			tempList.append(float(row[19]))
			tempList.append(float(row[20]))
			tempList.append(float(row[21]))
			tempList.append(float(row[22]))

			# print(tempList, "printed tempList for guards")

			allPlayerRtg.append(guardExRtg[index])
			allExStats.append(tempList)

	for index, f in enumerate(forwardExPlayer):
		if f == row[0]:
			tempList.append(float(row[7]))
			tempList.append(float(row[9]))
			tempList.append(float(row[11]))
			tempList.append(float(row[14]))
			tempList.append(float(row[15]))
			tempList.append(float(row[16]))
			tempList.append(float(row[17]))
			tempList.append(float(row[18]))
			tempList.append(float(row[19]))
			tempList.append(float(row[20]))
			tempList.append(float(row[21]))
			tempList.append(float(row[22]))

			allPlayerRtg.append(forwardExRtg[index])
			allExStats.append(tempList)

	for index, c in enumerate(centerExPlayer):
		if c == row[0]:
			tempList.append(float(row[7]))
			tempList.append(float(row[9]))
			tempList.append(float(row[11]))
			tempList.append(float(row[14]))
			tempList.append(float(row[15]))
			tempList.append(float(row[16]))
			tempList.append(float(row[17]))
			tempList.append(float(row[18]))
			tempList.append(float(row[19]))
			tempList.append(float(row[20]))
			tempList.append(float(row[21]))
			tempList.append(float(row[22]))

			allPlayerRtg.append(centerExRtg[index])
			allExStats.append(tempList)

	if len(tempList) == 0:
		continue
	else:
		tempList = []

X = np.array(allExStats)
y = np.array(allPlayerRtg)

clf.fit(X, y)

team = input("What team do you want to see? ")

#  printing first 5 rows

for row in rows:
	if row[1] == team:
		playerRoster.append( Player(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22]) )

for players in playerRoster:
	print(players.name, clf.predict( [[players.freeThrowPer, players.twoPointPer, players.threePointPer, players.pointsPerGame, players.reboundsPerGame, players.assistsPerGame, players.stealsPerGame, players.blocksPerGame, players.turnoversPerGame, players.versatilityIndex, players.offensiveRating, players.defensiveRating]] ) )
