import pandas
from sqlalchemy import create_engine
	
def pull(file):
	sched = pandas.read_csv(file);
	trunc = sched[["Week", "Winner/tie", "Loser/tie", "PtsW", "PtsL"]];
	con = create_engine("mysql+pymysql://root:@127.0.0.1/nfl2016"); 
	trunc.to_sql("nflgames2016", con, if_exists='replace', index=False);		
		
a = input("file name?");
b = "C:/users/yoshi/downloads/"+a;
pull (b);