import pandas as pd
import math

def sorter(file):
	df = pd.read_csv(file)
	td = (df[df["Play"].astype(str).str.contains('touchdown')])
	pat = (df[df["Play"].astype(str).str.contains('extra point')])
	fg = (df[df["Play"].astype(str).str.contains('field goal')])
	ko = (df[df["Play"].astype(str).str.contains('kicks off')])
	onside = (df[df["Play"].astype(str).str.contains('kicks onside')])
	punt = (df[df["Play"].astype(str).str.contains('punt')])
	sack = (df[df["Play"].astype(str).str.contains('sack')])
	penalty = (df[df["Play"].astype(str).str.contains('Penalty')])
	timeout = (df[df["Play"].astype(str).str.contains('Timeout')])
	clock = (df[df["Play"].astype(str).str.contains('spike')])
	throws = (df[df["Play"].astype(str).str.contains('pass')])
	runs = (df[df["Play"].astype(str).str.contains('Penalty')==False])
	runs = (runs[runs["Play"].astype(str).str.contains('pass')==False])
	runs = (runs[runs["Play"].astype(str).str.contains('kicks off')==False])
	runs = (runs[runs["Play"].astype(str).str.contains('sack')==False])
	runs = (runs[runs["Play"].astype(str).str.contains('punt')==False])
	runs = (runs[runs["Play"].astype(str).str.contains('extra point')==False])
	runs = (runs[runs["Play"].astype(str).str.contains('Timeout')==False])
	runs = (runs[runs["Play"].astype(str).str.contains('field goal')==False])
	runs = (runs[runs["Play"].astype(str).str.contains('spike')==False])
	number = len(pat.index)+len(fg.index)+len(ko.index)+len(onside.index)+len(punt.index)+len(sack.index)+len(penalty.index)+len(timeout.index)+len(clock.index)+len(throws.index)
	print (len(df.index), number , len(runs.index))
	col = ["Quarter", "Time Rem.", "Down", "Yards", "Location", "Poss", "Gun", "Form", "Play", "Away", "Home"]
	print (td[col])
#sorter("c:/users/yoshi/documents/python_scripts/nfl/pxp/games/201612040rav.csv")

def yard_adj(file):
	df = pd.read_csv(file)
	pos = df["Poss"]
	yard = df["Location"]
	yard = yard.fillna(method='ffill')
	for i in range(0, (len(pos.index))):
		pos[i] = pos[i].upper()
		if yard[i] == " 50":
			yard[i] = 50
		else:
			a = yard[i].split()[0]
			b = yard[i].split()[1]
		if pos[i] == "KO":
			yard[i] = b
		elif a == pos[i]:
			yard[i] = b
		else:
			yard[i] = 100- int(b)
	df["Location"] = yard
	df.to_csv(file)
yard_adj("c:/users/yoshi/documents/python_scripts/nfl/pxp/games/201612040rav.csv")