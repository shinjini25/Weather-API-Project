import requests
from twilio.rest import Client

account_sid= "AC2a1d8865b82abcc3aa4a92bab68c9aa2"
auth_token=   "f08f1a04e08a7c807acbc3599af90d78"

OVM_endpoint="https://api.openweathermap.org/data/2.5/onecall"

api_key="6c5ad75105956ce720b518cf35e282ed"

weather_params={
    "lat":19.075983, #put your location's latitude and longitude
    "lon":72.877655,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

is_cold = False

response=requests.get(OVM_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]   #for the next 12 hours only

for hour_data in weather_slice:
  condtition_code = hour_data["temp"]


  if condtition_code < 303.15:
     is_cold= True

if is_cold:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's kind of cold outside today, don't forget to bring in a jacket to keep yourself warm! :)",
        from_='+14844168061',
        to='+91 99693 71739'   #your phone number
    )
    print(message.status)


