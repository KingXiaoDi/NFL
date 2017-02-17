from team_info.name_converter import get_abr
from sqlalchemy import create_engine
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import numpy

def home_team(winner, loser, location):
	home = [];
	for i in range(0,16):
		if location[i] == "@":
			home.append(loser[i])#.lower());
		else:
			home.append(winner[i])#.lower());
	abr = [];
	for teams in home:
		abr.append(get_abr(teams));
	return (abr);
	
def date_formatter(year, date):
	formatted = []
	for dates in date:
		new = dates + " " + str(year);
		test = str(datetime.datetime.strptime(new, '%B %d %Y').date());
		test = test + "0";
		test = test.replace("-","");
		formatted.append(test);
	return formatted;
	
def yearly_sched(year, team):
	con = create_engine("mysql+pymysql://root:@127.0.0.1/nfl"); 
	sched = pd.read_sql("select `Date`, `Winner`, `Location`, `Loser` from `" + str(year)+"` where `Winner` = \""+team+"\" or `Loser` = \""+team+"\"", con);
	home = home_team(sched["Winner"], sched["Loser"], sched["Location"]);
	dates = date_formatter(year, sched["Date"]);
	url = [];
	for i in range(0,16):
		url.append(dates[i]+home[i]);
		url[i] = (url[i])[0]
	return url;
	#return (sched["Date"], home);
	#print (sched["Date"]);
	#print (sched["Winner"]);
	#print (sched["Location"]);
	#print (sched["Loser"]);
	

add = yearly_sched(2016, "Baltimore Ravens");
for i in add:
	site = "http://www.pro-football-reference.com/boxscores/"+i+".htm";
	print (site);