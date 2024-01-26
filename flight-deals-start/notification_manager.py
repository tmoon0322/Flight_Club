from twilio.rest import Client
import smtplib
import requests
import os

twilio_SID = os.environ["twilio_SID"]
twilio_auth_token = os.environ["twilio_auth_token"]
SHEETY_API_ENDPOINT = os.environ["SHEETY_API_ENDPOINT"]


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.init = True

    def send_text(self, price, departure_name, departure_code, arrival_name, arrival_code, outbound_date, inbound_date):
        client = Client(twilio_SID, twilio_auth_token)
        message = client.messages.create(
            from_='+18334551944',
            body=f"\n\nLow Price Alert!\nOnly ${price} to fly "
                 f"from {departure_name}-{departure_code} to {arrival_name}-{arrival_code} "
                 f"from {outbound_date} to {inbound_date}",
            to='+15106938176'
        )

    def send_emails(self,
                    price,
                    departure_name,
                    departure_code,
                    arrival_name,
                    arrival_code,
                    outbound_date,
                    inbound_date):
        response = requests.get(url=SHEETY_API_ENDPOINT)
        response.raise_for_status()
        data = response.json()
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="twinsmoon0322@gmail.com", password="randompassword")
            connection.sendmail(
                from_addr="twinsmoon0322@gmail.com",
                to_addrs="",
                msg=f"\n\nLow Price Alert!\nOnly ${price} to fly "
                    f"from {departure_name}-{departure_code} to {arrival_name}-{arrival_code} "
                    f"from {outbound_date} to {inbound_date}")



