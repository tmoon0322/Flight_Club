import requests
FLIGHT_API_KEY = "y6oq9QCN5l-_41bqA0_KVDqU6gDahLwr"
FLIGHT_API_ENDPOINT = "https://api.tequila.kiwi.com"
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.current_city = ""

    def city_search(self, city):
        self.current_city = city
        location_headers = {
            "apikey": FLIGHT_API_KEY
        }
        location_parameters = {
            "term": self.current_city
        }
        response = requests.get(url=f"{FLIGHT_API_ENDPOINT}/locations/query", headers=location_headers,
                                params=location_parameters)
        response.raise_for_status()
        data = response.json()
        code = data["locations"][0]["code"]
        return code






