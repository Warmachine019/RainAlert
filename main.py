import requests
import os
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY") #api key for the open weather map

account_sid = "ACCOUNT_SID"
auth_token = os.environ.get("AUTH_TOKEN") #Auth token for twilio

weather_params = {
    "lat": your_latitude_here,
    "lon": your_longitude_here,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        messaging_service_sid='MG1eb97cfe52a7488e68127275c03f4151',
        body="Its going to rain today. Take an umbrella with you.",
        to='YOUR_PHONE_NUMBER'
    )
    print(message.status)
