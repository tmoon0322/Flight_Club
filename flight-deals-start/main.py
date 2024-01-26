#This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
flight_searcher = FlightSearch()
if len(data_manager.sheet_data[0]["iataCode"]) < 1:
    for row in data_manager.sheet_data:
        city_name = row["city"]
        row["iataCode"] = flight_searcher.city_search(city=city_name)
    data_manager.update_codes()

flight_data_bot = FlightData()
notification_bot = NotificationManager()
for row in data_manager.sheet_data:
    city_code = row["iataCode"]
    city = row["city"]
    flight_price = flight_data_bot.get_flight_data(city_code=city_code)
    if flight_price is None:
        flight_price = flight_data_bot.get_flight_data(city_code=city_code, stop_overs=1)
        if flight_price is None:
            print(f"There are no flights to {city}")

    else:
        print(f"{city}: ${flight_price}")
        if row["lowestPrice"] > flight_price:
            pass
            notification_bot.send_emails(price=flight_price,
                                         arrival_code=city_code,
                                         arrival_name=city,
                                         departure_code="SFO",
                                         departure_name="San Francisco",
                                         inbound_date=flight_data_bot.inbound_date,
                                         outbound_date=flight_data_bot.outbound_date)

