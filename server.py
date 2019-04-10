#!/usr/bin/python3

from sanic import Sanic
from sanic.response import json
from standings import Standings

app = Sanic()


async def index(request):
    return json({'hello': 'world'})


async def standings_handler(request, league):
    standings = Standings(league)
    return json(standings.get_teams_array())

app.add_route(index, '/')
app.add_route(standings_handler, '/standings/<league>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
