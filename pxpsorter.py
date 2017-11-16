import pandas as pd
import math

def getRuns(df):
	runLocations = ['left end', 'right end', 'left tackle', 'right tackle', 'left guard', 'right guard', 'middle']
	runColumns = []
	for each in (df.columns.values):
		runColumns.append(each)
	newColumns = ["Player", "Direction", "Hole", "Gain"]
	for each in newColumns:
		runColumns.append(each)
	run = pandas.DataFrame(columns=runColumns)
	for each in runLocations:
		noPass = (df[df["Detail"].astype(str).str.contains('pass')==False])
		runPiece = noPass[noPass["Detail"].astype(str).str.contains(each)]
		for each in newColumns:
			runPiece[each] = ""
			#fix when you can read pandas docs
		run = run.append(runPiece)
	for each in run.iterrows():
		detailSplit= (each[1]["Detail"]).split(" ")
		gain = (detailSplit.index("for"))
		if "middle" in detailSplit:
			run.loc[each[0], "Direction"] = detailSplit[2]
			run.loc[each[0], "Hole"] = "center"
		else:
			run.loc[each[0], "Direction"] = detailSplit[2]
			run.loc[each[0], "Hole"] = detailSplit[3]
#		run.loc[each[0], "Gain"] = (detailSplit[gain+1])
		run.loc[each[0], "Gain"] = (detailSplit[gain+1])
		run.loc[each[0], "Player"] = detailSplit[0] + " " + detailSplit[1]
	print (run)
				
			
def sorter(df):
	td = (df[df["Detail"].astype(str).str.contains('touchdown')])
	pat = (df[df["Detail"].astype(str).str.contains('extra point')])
	fg = (df[df["Detail"].astype(str).str.contains('field goal')])
	ko = (df[df["Detail"].astype(str).str.contains('kicks off')])
	onside = (df[df["Detail"].astype(str).str.contains('kicks onside')])
	punt = (df[df["Detail"].astype(str).str.contains('punt')])
	sack = (df[df["Detail"].astype(str).str.contains('sack')])
	penalty = (df[df["Detail"].astype(str).str.contains('no play')])
	timeout = (df[df["Detail"].astype(str).str.contains('Timeout')])
	clock = (df[df["Detail"].astype(str).str.contains('spike')])
	#check how this is works
	throws = (df[df["Detail"].astype(str).str.contains('pass')])

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
