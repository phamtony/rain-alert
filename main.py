import requests
import os
from twilio.rest import Client

url = "https://api.openweathermap.org/data/2.5/onecall"
api = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("account_sid")
auth_token= os.environ.get("auth_token")

lat = 30.332184
long = -81.655647
parameters = {
    "lat": lat,
    "lon": long,
    "appid": api,
    "exclude": "current,minutely,daily"
}

response = requests.get(url, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
rain = False

for weather in weather_slice:
    if int(weather["weather"][0]["id"]) < 700:
        rain = True

if rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today! Remember to bring an umbrella",
        from_='+18064524372',
        to='+13233329156'
    )

    print(message.status)

#Use pythonanywhere and load this script, It'll be on the cloud and will run every day at 7AM