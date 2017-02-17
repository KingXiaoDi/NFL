from sqlalchemy import create_engine
from bs4 import BeautifulSoup
import pandas as pd
import requests
import datetime

def game_grabber(year):
	r = requests.get('http://www.pro-football-reference.com/years/'+str(year)+'/games.htm');
	made = BeautifulSoup(r.text, 'lxml');
	data = made.find("table", id = 'games');
	new = data.find_all('tbody');
	week = [];
	date = [];
	time = [];
	winner = [];
	location = [];
	loser = [];
	win_pts = [];
	loser_pts = [];
	win_to = [];
	loser_to = [];
	for stuff in data.find_all('th', {'data-stat': lambda x: x and x.startswith('week')}):
		week.append(stuff.text);
	week = [a for a in week if a != "Week"];
	for stuff in data.find_all('td', {'data-stat': lambda x: x and x.startswith('game_date')}):
		date.append(stuff.text);
	for stuff in data.find_all('td', {'data-stat': lambda x: x and x.startswith('gametime')}):
		time.append(stuff.text);
	for stuff in data.find_all('td', {'data-stat': lambda x: x and x.startswith('winner')}):
		winner.append(stuff.text);
	for stuff in data.find_all('td', {'data-stat': lambda x: x and x.startswith('game_location')}):
		location.append(stuff.text);
	for stuff in data.find_all('td', {'data-stat': lambda x: x and x.startswith('loser')}):
		loser.append(stuff.text);
	for stuff in data.find_all('td', {'data-stat': lambda x: x and x.startswith('pts_win')}):
		win_pts.append(stuff.text);
	for stuff in data.find_all('td', {'data-stat': lambda x: x and x.startswith('pts_lose')}):
		loser_pts.append(stuff.text);
	for stuff in data.find_all('td', {'data-stat': lambda x: x and x.startswith('to_win')}):
		win_to.append(stuff.text);
	for stuff in data.find_all('td', {'data-stat': lambda x: x and x.startswith('to_lose')}):
		loser_to.append(stuff.text);
	return (year, week, date, time, winner, location, loser, win_pts, loser_pts, win_to, loser_to);

def make_df(year, week, date, time, winner, location, loser, win_pts, loser_pts, win_to, loser_to):
	weeks = pd.Series(week);
	dates = pd.Series(date);
	times = pd.Series(time);
	winners = pd.Series(winner);
	losers= pd.Series(loser);
	winner_pts = pd.Series(win_pts);
	losers_pts = pd.Series(loser_pts);
	winner_to = pd.Series(win_to);
	losers_to = pd.Series(loser_to);
	locations = pd.Series(location);
	df = pd.DataFrame();
	df['Week'] = weeks.values;
	df['Date'] = dates.values;
	df['Time'] = times.values;
	df['Winner'] = winners.values;
	df['Location'] = locations.values;
	df['Loser'] = losers.values;
	df['Pts (W)'] = winner_pts.values;
	df['Pts (L)'] = losers_pts.values;
	df['TO (W)'] = winner_to.values;
	df['TO (L)'] = losers_to.values;
	return (year, df);
	
def date_formatter(year, week, date, time, winner, location, loser, win_pts, loser_pts, win_to, loser_to):
	new = date[0].split();
	print (new);

def to_sql(year, frame):
	con = create_engine("mysql+pymysql://root:@127.0.0.1/nfl"); 
	frame.to_sql(str(year), con, if_exists = 'append', index=False);
for i in range(2016, 2017):
	date_formatter(*game_grabber(i));