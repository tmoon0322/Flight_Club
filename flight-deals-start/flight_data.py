import datetime as dt
import requests
import os
from pprint import pprint
FLIGHT_API_KEY = os.environ["FLIGHT_API_KEY"]
FLIGHT_API_ENDPOINT = os.environ["FLIGHT_API_ENDPOINT"]
tomorrow_date = dt.date.today() + dt.timedelta(days=1)
tomorrow = tomorrow_date.strftime("%d/%m/%Y")
six_months_later_date = dt.date.today() + dt.timedelta(days=180)
six_months_later = six_months_later_date.strftime("%d/%m/%Y")


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.price = 0
        self.departure_airport_code = ""
        self.departure_city = ""
        self.outbound_date = ""
        self.inbound_date = ""

    def get_flight_data(self, city_code, stop_overs=0):
        search_headers = {
            "apikey": FLIGHT_API_KEY
        }
        search_parameters = {
            "fly_from": "SFO",
            "fly_to": city_code,
            "date_from": tomorrow,
            "date_to": six_months_later,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "max_stopovers": stop_overs,
            "curr": "USD",
            "sort": "price",
            "limit": 1
        }
        response = requests.get(url=f"{FLIGHT_API_ENDPOINT}/search", params=search_parameters, headers=search_headers)
        response.raise_for_status()
        data = response.json()
        if stop_overs == 0:
            try:
                self.price = data["data"][0]["price"]
                outbound = data["data"][0]["route"][0]["local_departure"]
                inbound = data["data"][0]["route"][1]["local_departure"]
                outbound_list = outbound.split("T")
                inbound_list = inbound.split("T")
                self.outbound_date = outbound_list[0]
                self.inbound_date = inbound_list[0]
            except IndexError:
                return None
            else:
                return self.price
        else:
            try:
                self.price = data["data"][0]["price"]
                outbound = data["data"][0]["route"][0]["local_departure"]
                inbound = data["data"][0]["route"][1]["local_departure"]
                outbound_list = outbound.split("T")
                inbound_list = inbound.split("T")
                self.outbound_date = outbound_list[0]
                self.inbound_date = inbound_list[0]
            except IndexError:
                return None
            else:
                return self.price








