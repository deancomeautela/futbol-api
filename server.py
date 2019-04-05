#!/usr/bin/env python3

from sanic import Sanic
from sanic.response import json

app = Sanic()

@app.route('/')
async def test(request):
  return json({'hello': 'world'})

if __name__ == '__main__':
  app.run(hos0t='0.0.0.0', port=3000)
