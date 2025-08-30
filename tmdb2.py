import requests


class TMDBClient:
    BASE_URL = "https://api.themoviedb.org/3"

    def __init__(self, api_key):
        self.api_key = api_key

    def _make_request(self, endpoint, params=None):
        if params is None:
            params = {}
        params['api_key'] = self.api_key
        response = requests.get(f"{self.BASE_URL}{endpoint}", params=params)
        response.raise_for_status()
        return response.json()

    def search_movies(self, query, page=1):
        endpoint = "/search/movie"
        params = {
            'query': query,
            'page': page
        }
        return self._make_request(endpoint, params)

    def get_popular_movies(self, page=1):
        endpoint = "/movie/popular"
        params = {'page': page}
        return self._make_request(endpoint, params)


def print_movies(movies):
    for movie in movies['results']:
        print(f"Title: {movie['title']}")
        print(f"Release Date: {movie['release_date']}")
        print(
            f"Overview: {movie['overview'][:100]}...")  # Print first 100 characters of overview
        print(f"Vote Average: {movie['vote_average']}")
        print("---")


def main():
    api_key = "29cde7de8b05b8d327ecfd1f0b426cec"  # Replace with your actual API key
    client = TMDBClient(api_key)

    while True:
        print("\n1. Search for movies")
        print("2. Get popular movies")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            query = input("Enter search query: ")
            results = client.search_movies(query)
            print_movies(results)
        elif choice == '2':
            results = client.get_popular_movies()
            print_movies(results)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
