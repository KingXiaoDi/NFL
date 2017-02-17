import pandas as pd

def get_abr(name):
	df = pd.read_csv("c:/users/Josh/Documents/Python_Scripts/nfl/pxp/team_info/team_info.csv");
	return df.loc[df['Team'] == name]['Abr'].values;
	a = df.loc[df['Team'] == name]['Abr'].values
	print (type(a));