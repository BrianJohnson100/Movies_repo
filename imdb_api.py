from collections import defaultdict
import pprint
import csv
import http.client
import json


class TMDBAPIUtils:

    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_movie_cast(self, movie_id: str, limit: int = None,
                       exclude_ids: list = None) -> list:

        conn = http.client.HTTPSConnection("api.themoviedb.org")
        conn.request("GET",
                     f"/3/movie/{movie_id}/credits?api_key="
                     f"{self.api_key}&language=en-US")

        response = conn.getresponse()
        data = response.read().decode("utf-8")
        credits = json.loads(data)
        cast = [
            {"id": str(member["id"]), "character": member.get("character", ""),
             "name": member.get("name", ""),
             "credit_id": member.get("credit_id", ""),
             "order": member.get("order", "")} for member in
            credits.get("cast", [])]
        if exclude_ids is None:
            exclude_ids = []
        if limit is None:
            limit = float('inf')
        cast = [member for member in cast if
                (int(member["id"]) not in exclude_ids) and (
                        0 <= member["order"] < limit)]  # 1.2
        return cast

    def get_movie_credits_for_person(self, person_id: str,
                                     vote_avg_threshold: float = None) -> list:

        if vote_avg_threshold is None:
            vote_avg_threshold = 0.0

        conn = http.client.HTTPSConnection("api.themoviedb.org")
        conn.request("GET",
                     f"/3/person/{person_id}/movie_credits?api_key="
                     f"{self.api_key}&language=en-US")

        response = conn.getresponse()
        data = response.read().decode("utf-8")
        credits = json.loads(data)
        pprint.pprint(credits)
        # exit()

        movie_credits = [
            {"id": str(credit["id"]), "title": credit.get("title", ""),
             "vote_avg": credit.get("vote_average", "")} for credit in
            credits.get("cast", []) if str(credit["id"]) == person_id]
        return movie_credits


if __name__ == "__main__":
    tmdb_api_utils = TMDBAPIUtils(api_key='29cde7de8b05b8d327ecfd1f0b426cec')
    movie_credits = tmdb_api_utils.get_movie_credits_for_person('2975')
    print(dir(tmdb_api_utils))