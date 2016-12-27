import pandas
from sqlalchemy import create_engine
import os.path

#Get list of team names; also includes conference, division, and abbreviation for future use
teams = pandas.read_csv("c:/users/yoshi/downloads/teamlist.csv");
teams.index.name = "TeamID"
Teams = teams["Team"]

#Search database for results by team, return wins, losses, tie; still need to improve format. Goal: Tm, W-L-T
def get_record(team):
	con = create_engine("mysql+pymysql://root:@127.0.0.1/nfl2016"); 
	wins = pandas.read_sql("select `Winner/tie` as Team, count(Week) as W from `nflgames2016` where `Winner/tie` =\""+str(team)+"\" and PtsW > PtsL", con);
	losses = pandas.read_sql("select `Loser/tie` as Team, count(Week) as L from `nflgames2016` where `Loser/tie` =\""+str(team)+"\" and PtsW > PtsL", con);
	ties = pandas.read_sql("select count(Week) as T from `nflgames2016` where (`Winner/tie` =\""+str(team)+"\" or `Loser/tie` =\""+str(team)+"\") and PtsW = PtsL", con);
	record = pandas.merge(wins, losses, how='left', on='Team');
	#leftties = pandas.merge(record, ties, how='left', left_on='Team', right_on='TeamA');
	record = record.join(ties);
	return record;
	
#Send team results to CSV for easy viewing	
def make_standings(file, team):
	if os.path.isfile(file) == True:
		team.to_csv(loc, mode='a', index=False, header=False);
	else: 
		team.to_csv(loc, mode='w', index=False);
name = input("filename?");
loc = "c:/users/yoshi/downloads/"+str(name)+".csv";

for i in Teams:
	get_record(i);
	#make_standings(loc, get_record(i));
print (teams);