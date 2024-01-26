import requests
from pprint import pprint
import os

GOOGLE_SHEET_NAME = "prices"
SHEETY_API_ENDPOINT = os.environ["SHEETY_API_ENDPOINT_PRICES"]


class DataManager:
    def __init__(self):
        response = requests.get(url=SHEETY_API_ENDPOINT)
        response.raise_for_status()
        self.sheet_name = "prices"
        self.data = response.json()
        self.sheet_data = self.data["prices"]

    def update_codes(self):
        for city in self.sheet_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"https://api.sheety.co/9357f34c310b67b0be01a56b1680e5c9/flightDeals/prices/{city['id']}",
                json=new_data
            )
            response.raise_for_status()
            print(response.text)



