import requests


class GetRequester:
    def __init__(self, url="https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"):
        self.url = url
        self.response = None

    def get_response(self):
        """Fetches and caches the HTTP response from the endpoint."""
        if self.response is None:
            self.response = requests.get(self.url)
        return self.response

    def get_response_body(self):
        """Queries endpoint and returns raw response body (bytes)."""
        res = self.get_response()
        return res.content

    def load_json(self):
        """Converts raw endpoint data to Python JSON objects (dicts/lists)."""
        res = self.get_response()
        return res.json()