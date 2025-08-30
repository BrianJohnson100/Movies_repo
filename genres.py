import requests

url = "https://api.themoviedb.org/3/genre/movie/list?language=en"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyOWNkZTdkZThiMDViOGQzMjdlY2ZkMWYwYjQyNmNlYyIsIm5iZiI6MTcyNjkzOTUzOS4xODcsInN1YiI6IjY2ZWYwMTkzYjM0OGJlYTRlYjNiMjBhMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.b6WABGHZoaeXb679x5XYyhNE7z05vUUVPUt3eqwL-2o"
}

response = requests.get(url, headers=headers)

print(response.text)