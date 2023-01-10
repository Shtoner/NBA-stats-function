import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import urllib.request

def get_player_stats():
  year=input("Which NBA season are you interested in?: ")
  player=input("For which player do you want to get stats?: ")
  #print(player)
    #fetch url
  url = 'https://www.basketball-reference.com/leagues/'
  #get it to readable form   
  r = requests.get(url)
  r_html = r.text
  soup = BeautifulSoup(r_html,  'html.parser')
  #whole table
  #souptable=soup.find_all(scope="row")
  for tag in soup.findAll('a', text=re.compile(year)):
    if tag.parent.name == 'th':
      htm2=urllib.request.urlopen('https://www.basketball-reference.com' + tag["href"]).read()
      # print(tag["href"])
      # print(htm2)

  soup2=BeautifulSoup(htm2)
  pergameLink=soup2.find('a', text=re.compile('Per Game'))
  htm3= urllib.request.urlopen('https://www.basketball-reference.com' + pergameLink.get('href')).read()
  # print(pergameLink.get('href'))


  soup3=BeautifulSoup(htm3)
  # print(soup3)
  # target html element(top column of table)
  head=soup3.find(class_="thead")
  #make it more readable
  column_names_raw=[head.text for item in head][0]
  column_names_raw=[head.text for item in head][0]
  column_names_polished=column_names_raw.replace("\n",",").split(",")[2:-1]
  column_names_polished

  table=soup3.find_all(class_="full_table")
  players=[]
  for i in range(len(table)):
          
          
          player_=[]
          
          for td in table[i].find_all("td"):
              player_.append(td.text)
      
          players.append(player_)
  x=tuple(players)
  y=tuple(column_names_polished)
  # df=pd.DataFrame(x, columns=y).set_index("Player")
  df=pd.DataFrame(players, columns=column_names_polished).set_index("Player")
  pd.set_option('display.max_columns', None)
  #print(souptable)
  fd=df[df.index.str.startswith(player)]
  print(fd)
  
get_player_stats()
  
def get_NBA_stats():
  year=input("Which NBA season are you interested in?: ")
  url = 'https://www.basketball-reference.com/leagues/'
  #get it to readable form   
  r = requests.get(url)
  r_html = r.text
  soup = BeautifulSoup(r_html,  'html.parser')
  #whole table
  #souptable=soup.find_all(scope="row")
  for tag in soup.findAll('a', text=re.compile(year)):
    if tag.parent.name == 'th':
      htm2=urllib.request.urlopen('https://www.basketball-reference.com' + tag["href"]).read()
      # print(tag["href"])
      # print(htm2)

  soup2=BeautifulSoup(htm2)
  pergameLink=soup2.find('a', text=re.compile('Per Game'))
  htm3= urllib.request.urlopen('https://www.basketball-reference.com' + pergameLink.get('href')).read()


  soup3=BeautifulSoup(htm3, features="html.parser")
  # print(soup3)
  # target html element(top column of table)
  head=soup3.find(class_="thead")
  #make it more readable
  column_names_raw=[head.text for item in head][0]
  column_names_raw=[head.text for item in head][0]
  column_names_polished=column_names_raw.replace("\n",",").split(",")[2:-1]
  column_names_polished

#dump all players' stats into players variable
  table=soup3.find_all(class_="full_table")
  players=[]
  for i in range(len(table)):
          
          
          player_=[]
          
          for td in table[i].find_all("td"):
              player_.append(td.text)
      
          players.append(player_)
  x=tuple(players)
  y=tuple(column_names_polished)
  df=pd.DataFrame(players, columns=column_names_polished).set_index("Player")
  pd.set_option('display.max_rows', None)
  pd.set_option('display.max_columns', None)
  df.to_csv('data/raw_data2022.csv', index=True)
#   df.to_excel('raw_data.xls', index=False)
  print(df)


