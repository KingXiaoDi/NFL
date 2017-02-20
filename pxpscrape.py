from selenium.webdriver.common.keys import Keys
from pxp_url_maker import yearly_sched
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

def get_pxp(save_name):
	driver = webdriver.Chrome(executable_path="C:/Users/Yoshi/Documents/Python_Scripts/chrome/chromedriver.exe")
	url = ("http://www.pro-football-reference.com/boxscores/"+save_name+".htm")
	driver.get(url)
	r = driver.page_source
	soup = BeautifulSoup(r, "lxml")
	driver.quit()
	data = soup.find("table", id = 'pbp')
	new = data.find_all('tbody')
	quarter = []
	time_rem = []
	down = []
	yards = []
	location = []
	play = []
	away_sc = []
	home_sc = []
	for stuff in data.find_all('th', {'data-stat': lambda x: x and x.startswith('quarter')}):
		quarter.append(stuff.text)
	quarter = [a for a in quarter if a != "Quarter"]
	for stuff in data.find_all('td', {'data-stat': lambda x: x and x.startswith('qtr_time')}):
		time_rem.append(stuff.text)
	for stuff in data.find_all('td', {'data-stat': lambda x: x and x.startswith('down')}):
		down.append(stuff.text)
	for stuff in data.find_all('td', {'data-stat': lambda x: x and x.startswith('yds')}):
		yards.append(stuff.text)
	for stuff in data.find_all('td', {'data-stat': lambda x: x and x.startswith('location')}):
		location.append(stuff.text)
	for stuff in data.find_all('td', {'data-stat': lambda x: x and x.startswith('detail')}):
		play.append(stuff.text)
	for stuff in data.find_all('td', {'data-stat': lambda x: x and x.startswith('pbp_score_aw')}):
		away_sc.append(stuff.text)
	for stuff in data.find_all('td', {'data-stat': lambda x: x and x.startswith('pbp_score_hm')}):
		home_sc.append(stuff.text)
	return (quarter, time_rem, down, yards, location, play, away_sc, home_sc, save_name)
	
def save_values(quarter, time_rem, down, yards, location, play, away_sc, home_sc, save_name):
	quarters = pd.Series(quarter)
	time_left = pd.Series(time_rem)
	down1 = pd.Series(down)
	yards1 = pd.Series(yards)
	loc = pd.Series(location)
	play1 = pd.Series(play)
	vis_sc = pd.Series(away_sc)
	hm_sc = pd.Series(home_sc)
	df = pd.DataFrame()
	df['Quarter'] = quarters.values
	df['Time Rem.'] = time_left.values
	df['Down'] = down1.values
	df['Yards'] = yards1.values
	df['Location'] = loc.values
	df['Play'] = play1.values
	df['Away'] = vis_sc.values
	df['Home'] = hm_sc.values
	df.to_csv('c:/users/yoshi/documents/python_scripts/nfl/pxp/games/'+str(save_name)+'.csv')

for games in yearly_sched(2016, "Baltimore Ravens"):
	save_values(*get_pxp(games))