import requests
import pandas as pd
from bs4 import Comment, BeautifulSoup
 
r = requests.get("http://www.pro-football-reference.com/boxscores/201612250pit.htm")
 
b = BeautifulSoup(r.text, "lxml")
 
 
l = b.find("div", { "id" : "all_pbp" } )
comments = l.findAll(text=lambda text:isinstance(text, Comment))
 
commentsoup = BeautifulSoup(comments[0], "lxml")

df = pd.read_html(str(commentsoup))[0];
df = df[["Quarter", "Time", "Down", "ToGo", "Location", "Detail", "BAL", "PIT"]];

#df.to_csv("c:/users/yoshi/documents/python scripts/pbp.csv");

throw = (df[df["Detail"].astype(str).str.contains('pass')]);
ko = (df[df["Detail"].astype(str).str.contains('kicks off')]);
onside = (df[df["Detail"].astype(str).str.contains('kicks onside')]);
punt = (df[df["Detail"].astype(str).str.contains('punt')]);
sack = (df[df["Detail"].astype(str).str.contains('sack')]);
penalty = (df[df["Detail"].astype(str).str.contains('Penalty')]);
other = (df[df["Detail"].astype(str).str.contains('Penalty')==False]);
other = (other[other["Detail"].astype(str).str.contains('pass')==False]);
print (punt);
