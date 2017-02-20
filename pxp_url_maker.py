from sqlalchemy import create_engine
from bs4 import BeautifulSoup
import pandas as pd
import datetime

def get_abr(name):
	df = pd.read_csv("c:/users/yoshi/Documents/Python_Scripts/nfl/pxp/team_info/team_info.csv")
	return df.loc[df['Team'] == name]['Abr'].values
	a = df.loc[df['Team'] == name]['Abr'].values
	
def home_team(winner, loser, location, games):
	home = []
	for i in range(0,games):
		if location[i] == "@":
			home.append(loser[i])#.lower())
		else:
			home.append(winner[i])#.lower())
	abr = []
	for teams in home:
		abr.append(get_abr(teams))
	return (abr)
	
def date_formatter(year, date):
	formatted = []
	for dates in date:
		new = dates + " " + str(year)
		test = datetime.datetime.strptime(new, '%B %d %Y').date()
		if test.month == 1 or test.month == 2:
			new = dates + " " + str(year+1)
			test = datetime.datetime.strptime(new, '%B %d %Y').date()
		test = str(test) + "0"
		test = test.replace("-","")
		formatted.append(test)
	return formatted
	
def yearly_sched(year, team):
	con = create_engine("mysql+pymysql://root:@127.0.0.1/nfl") 
	sched = pd.read_sql("select `Date`, `Winner`, `Location`, `Loser` from `" + str(year)+"` where `Winner` = \""+team+"\" or `Loser` = \""+team+"\"", con)
	games = len(sched.index)
	home = home_team(sched["Winner"], sched["Loser"], sched["Location"], games)
	dates = date_formatter(year, sched["Date"])
	url_ending = []
	for i in range(0,games):
		url_ending.append(dates[i]+home[i])
		url_ending[i] = (url_ending[i])[0]
	return url_ending