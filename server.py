#!/usr/bin/python3

from sanic import Sanic
from sanic.response import json
from standings import Standings

app = Sanic()

async def standings_handler(request, league):
    standings = Standings(league)
    return json(standings.get_league_standings())

app.add_route(standings_handler, '/standings/<league>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
