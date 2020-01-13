import json
from pathlib import Path

# read a json file
data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies[0]["title"])

# write a json file
# movies = [
# 	{"id": 1, "title": "Terminator", "year": 1984},
# 	{"id": 2, "title": "Kindergarten Cop", "year": 1993}
# ]


# data = json.dumps(movies)
# Path("movies.json").write_text(data)