#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup


class Standings:

    def __init__(self, league):
        self.league = league

    def get_teams(self):
        url = 'http://www.espn.com/soccer/table/_/league/' + self.league + '.1'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        teams = soup.find_all(class_='team-link flex items-center clr-gray-03')
        return teams

    def get_name(self, team):
        return team.a.img.get('title')

    def get_position(self, team):
        return team.find(class_='team-position ml2 pr3').text

    # returns response to the api as an array of dictionaries containing
    # the team names and their position from the leage specified
    def get_league_standings(self):
        teams = self.get_teams()
        names = map(self.get_name, teams)
        positions = map(self.get_position, teams)
        teams_array = []
        for name, position in zip(names, positions):
            teams_array.append({'team': name, 'position': int(position)})
        if not teams_array:
            message = 'League ' + self.league.upper() + ' not found'
            code = 204
        else:
            message = 'Standigs for ' + self.league.upper()
            code = 200
        response = {
            'code': code,
            'message': message,
            'teams': teams_array
            }
        return response
