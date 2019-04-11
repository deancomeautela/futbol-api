# This is a futbol API

Currently it only works for league standings.

# How to use:
 - You make a `GET` request to the server and the api will respond with a JSON with the league standings for the league requested, which for a good request will look something like this:
   ```json
    {
        "message": "Standings for ESP",
        "code": 200,
        "teams": [
            {
                "position": 1,
                "team": "Barcelona"
            },
            {
                "position": 2,
                "team": "Atletico Madrid"
            }
        ]
    }
   ```
   If the League you are looking for doesn't exist the response will look like this:
   ```json
    {
        "code": 204,
        "message": "League ASDF not found"
    }
   ```
 - The request will look something like this:
   - `localhost:8080/standings/<league>`
- League is the abbreviation of the leagues name, for example Spain would be `esp`, BPL would be `eng`, Series A would be `ita`, and so on.