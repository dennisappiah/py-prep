import json
from pathlib import Path

movies = [
    {"id": 1, "title":"Terminator", "year": 1998},
    {"id": 2, "title":"Anaconda", "year": 1990},
   {"id": 3, "title":"Hello", "year": 1999},
]

# convert movie object into json string and write to movies.json (marshaling)
data = json.dumps(movies)
Path("movies.json").write_text(data)

# convert from json string to object (unmarshaling)
data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies)
