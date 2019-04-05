#!usr/bin/env python3

import requests
from bs4 import BeautifulSoup

url = 'http://www.espn.com/soccer/table/_/league/mex.1'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

def get_name(team):
  return team.a.img.get('title')

def get_position(team):
 return team.find(class_='team-position ml2 pr3').text

def get_table(teams):
  names = map(get_name, teams)
  positions = map(get_position, teams)
  return { positions: positions, names: names }

def get_teams_as_dictionary(teams):
  names = list(map(get_name, teams))
  positions = map(get_position, teams)
  teamsDict = {}
  for name, position in zip(names, positions):
    teamsDict[name] = { 'position': position }
  return teamsDict

teams = soup.find_all(class_='team-link flex items-center clr-gray-03')

titles = list(map(get_name, teams))
positions = map(get_position, teams)
teamsPT = get_table(teams)

teamsDict = get_teams_as_dictionary(teams)

print(teamsDict)

#for title, position in zip(titles, positions):
  #print('title:', title, '\nposition:', position)

#print(teamsPT)
