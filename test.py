import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

#search = input("Enter search term:\n>")
search = 'mercedes lackey'
try:
	isinstance(search, str)
except:
	print ("Strings only please!")

#pages = input("Enter how many pages you'd like to automate (note that large numbers will obviously take longer):\n>")
pages = 1
try:
	pages = int(pages)
except ValueError:
	print ("Please enter an integer!")
	
url_list = []
book_names = []
author = []
dl_url = []

for x in range(1,pages+1):
	post_titles = []
	urls = []
	url = 'http://audiobookbay.me/page/{}/?s={}'.format(x, search)
	page = requests.get('http://audiobookbay.me/page/{}/?s={}'.format(x, search), auth=('PyPyTset', 'PyTester123'))
	soup = BeautifulSoup(page.text, 'lxml')
	soup.encode('utf-8')

	search_results = soup.find_all('div', class_='post')
	for x in search_results: 
		post_titles.append(x.find('div', class_='postTitle'))
	
	for y in post_titles:
		urls.append(y.find('a'))
#		text = str(y.get_text())
#		text = re.sub('\u2019', "'", text)
		title, name = y.get_text().split('-', maxsplit = 1)
		book_names.append(title)
		author.append(name)
	for z in urls:
		url_add = 'http://audiobookbay.me'+str(z['href'])
		url_list.append(url_add)

for x in url_list:
	try:
		saved = pd.read_csv('c:/users/josh/documents/test.csv')
	except:
		saved = pd.DataFrame
	page2 = pd.read_html(x)
	db = pd.DataFrame(page2[0])
	print (db[15:17])
	
#	page2[0].to_csv('c:/users/josh/documents/test.csv', mode = 'a')
	
book_data = pd.DataFrame({'Title': book_names, 'Author': author})
#book_data.to_csv('c:/users/josh/documents/test.csv')