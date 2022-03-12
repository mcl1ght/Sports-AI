#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 13:11:55 2022

@author: Mclight
"""
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

numrows = len(rows) 
#we used the first half of the rows for the training data
training_data = np.array(rows[:numrows//2])
#we used the last half for the testing data
testing_data = np.array(rows[numrows//2:])

input_cols = (4,5) #arbitrary stats for testing 
output_col = 2 #chose the position as the output

clf.fit(training_data[:,input_cols], training_data[:, output_col])