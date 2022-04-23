# Import the machine learning "classifier" we want to test.
from decimal import Decimal
from tokenize import Double
from sklearn.ensemble import RandomForestClassifier
# Import the numpy package with "np" as an alias.
import numpy as np
import csv

# Create an "classifier" object which will try to "learn" our function

guardPosition = RandomForestClassifier()
guardExStats = []

forwardPosition = RandomForestClassifier()
forwardExStats = []

centerPosition = RandomForestClassifier()
centerExStats = []

allPositions = RandomForestClassifier()
allExStats = []
allExRatings = []

playerRoster = []
rankedRoster = []

class Player:
	def __init__(self, NAME, TEAM, POS, AGE, GP, MPG, FTA, FTP, TWPA, TWPP, THPA, THPP, eFG, TS, PPG, RPG, APG, SPG, BPG, TOPG, VI, ORTG, DRTG, RTG):
		self.name = NAME
		self.team = TEAM
		self.position = POS
		self.age = AGE
		self.gamesPlayed = GP
		self.minPerGame = MPG
		self.rating = int(RTG)

		self.stats = []
		self.stats.append( float(FTP) )
		self.stats.append( float(TWPP) )
		self.stats.append( float(THPP) )
		self.stats.append( float(PPG) )
		self.stats.append( float(BPG) )
		self.stats.append( float(APG) )
		self.stats.append( float(SPG) )
		self.stats.append( float(BPG) )
		self.stats.append( float(TOPG) )
		self.stats.append( float(VI) )
		self.stats.append( float(ORTG) )
		self.stats.append( float(DRTG) )

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
# NAME, TEAM, POS, AGE, GP, MPG, FTA, FT%, 2PA, 2P%, 3PA, 3P%, eFG%, TS%, PPG, RPG, APG, SPG, BPG, TOPG, VI, ORTG, DRTG

guardExPlayer = ["Stephen Curry", "Kyrie Irving", "Zach LaVine", "De'Aaron Fox", "Russell Westbrook", "Pat Connaughton", "Markus Howard", "Spencer Dinwiddie"]
guardExRtg = [96, 91, 88, 84, 78, 73, 67, 82]

forwardExPlayer = ["Giannis Antetokounmpo", "Jayson Tatum", "Domantas Sabonis", "Miles Bridges", "Kelly Oubre Jr.", "Justin Holiday", "CJ Elleby", "Jimmy Butler", "Kevin Durant"]
forwardExRtg = [96, 90, 87, 84, 78, 73, 68, 91, 96]

centerExPlayer = ["Nikola Jokic", "Karl-Anthony Towns", "Deandre Ayton", "Steven Adams", "DeMarcus Cousins", "Kai Jones", "Tacko Fall", "Boban Marjanovic"]
centerExRtg = [95, 89, 86, 83, 78, 72, 71, 74]

guardExRtgInOrder = []
forwardExRtgInOrder = []
centerExRtgInOrder = []

tempList = []

# Go through all the example players and add their stats to an array
# of all the stats the computer will read
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

            guardExRtgInOrder.append(guardExRtg[index])
            guardExStats.append(tempList)
            allExRatings.append(guardExRtg[index])
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

            forwardExRtgInOrder.append(forwardExRtg[index])
            forwardExStats.append(tempList)
            allExRatings.append(forwardExRtg[index])
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

            centerExRtgInOrder.append(centerExRtg[index])
            centerExStats.append(tempList)
            allExRatings.append(centerExRtg[index])
            allExStats.append(tempList)

    tempList = []

# fit the guard stats
guardPosition.fit(guardExStats, guardExRtgInOrder)

# fit the forward stats
forwardPosition.fit(forwardExStats, forwardExRtgInOrder)

# fit the center stats
centerPosition.fit(centerExStats, centerExRtgInOrder)

# fit all the stats to all the players
allPositions.fit(allExStats, allExRatings)

team = input("What team do you want to see? ")
playerNames = []

# create a player object for every player on the selected team
for row in rows:
	if row[1] == team or row[0] == team:
		if len(row) == 23 or row[23] == '':
			playerRoster.append( Player(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], '0') )
		elif len(row) == 24:
			playerRoster.append( Player(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23]) )
		playerNames.append(row[0])
print('')

toSee = input("Do you want to see the players in their best position, the position they play, or their comparasion to all positions\n(best, play, compare): ")

if toSee == "play":
    print("\nWhat they currently play:")
    for players in playerRoster:
        if players.position == "G":
            print(players.name, guardPosition.predict( [players.stats] ), "as a guard")
        if players.position == "F":
            print(players.name, forwardPosition.predict( [players.stats] ), "as a forward")
        if players.position == "C":
            print(players.name, centerPosition.predict( [players.stats] ), "as a center")

if toSee == "best":
    print("\nIn their best position:")
    for players in playerRoster:
        bestPos = "N"
        bestVal = 0
        if guardPosition.predict( [players.stats] ) >= bestVal:
            bestVal = guardPosition.predict( [players.stats] )
            bestPos = "G"
        if forwardPosition.predict( [players.stats] ) >= bestVal:
            bestVal = forwardPosition.predict( [players.stats] )
            bestPos = "F"
        if centerPosition.predict( [players.stats] ) >= bestVal:
            bestVal = centerPosition.predict( [players.stats] )
            bestPos = "C"
        
        if bestPos == "G":
            print(players.name, bestVal, "as a guard")
        if bestPos == "F":
            print(players.name, bestVal, "as a forward")
        if bestPos == "C":
            print(players.name, bestVal, "as a center")

if toSee == "compare":
    print("\nCompared to every position:")
    for players in playerRoster:
        print("\n")
        print(players.name, guardPosition.predict( [players.stats] ), "as a guard")
        print(players.name, forwardPosition.predict( [players.stats] ), "as a forward")
        print(players.name, centerPosition.predict( [players.stats] ), "as a center")
        print(players.name, allPositions.predict( [players.stats] ), "overall")
