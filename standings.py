import pandas
from sqlalchemy import create_engine

#Get list of team names; also includes conference, division, and abbreviation for future use
teams = pandas.read_csv("C:/Users/Josh/Documents/Python Scripts/nfl/teamlist.csv");
teams.index.name = "TeamID"
Teams = teams["Team"]

#send Team, Abr, Conference, and Division to a Team Table in SQL database
#create "NFL" database separate from "nfl2016?" would require change to con definition, probably valuable
def team_table(frame):
	con = create_engine("mysql+pymysql://root:@127.0.0.1/nfl2016");

#Search database for results by team, return wins, losses, tie; still need to improve format. Goal: Tm, W-L-T
def get_record(team):
	con = create_engine("mysql+pymysql://root:@127.0.0.1/nfl2016"); 
	wins = pandas.read_sql("select `Winner/tie` as Team, count(Week) as W from `nflgames2016` where `Winner/tie` =\""+str(team)+"\" and PtsW > PtsL", con);
	losses = pandas.read_sql("select `Loser/tie` as Team, count(Week) as L from `nflgames2016` where `Loser/tie` =\""+str(team)+"\" and PtsW > PtsL", con);
	ties = pandas.read_sql("select count(Week) as T from `nflgames2016` where (`Winner/tie` =\""+str(team)+"\" or `Loser/tie` =\""+str(team)+"\") and PtsW = PtsL", con);
	record = pandas.merge(wins, losses, how='left', on='Team');
	record = record.join(ties);
	return record;
	
#Send team results to CSV for easy viewing; used to check results easily, extraneous step to be removed (send directly to SQL)	
def make_standings(team_list):
	update = pandas.DataFrame(columns = ["Team", "W", "L", "T"]);    #create empty frame to hold updated record data
	for i in team_list:
		update = update.append(get_record(i), ignore_index=True);		#add each team's updated record data to the frame
	update = update.sort_values(by=["W", "L"], ascending = [0, 1]); #sort the frame by W/L (team with most wins, then fewest losses)
	return update;
	
#Send standings to SQL
def update_sql(teams):
	con = create_engine("mysql+pymysql://root:@127.0.0.1/nfl2016");
	make_standings(teams).to_sql("stand2016", con, if_exists='replace', index=False);
update_sql(Teams);	
print (make_standings(Teams));
