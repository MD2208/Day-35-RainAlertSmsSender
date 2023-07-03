import requests
from twilio.rest import Client
# Geolocation of krakow
MY_LAT = 50.064651 
MY_LONG = 19.944981
# Twilio Auth ID and Key to send sms
MY_SID = 'your-auth-sid'
MY_TOKEN = 'your-auth-token' 
MY_NUMBER = 'your-twilio-number'
# api req
my_api_key = 'your-open-weather-api-key'
api_url = 'https://api.openweathermap.org/data/2.5/forecast'

params={
    'lat':MY_LAT,
    'lon':MY_LONG,
    'appid':my_api_key
}

my_req = requests.get(url=api_url, params=params)
my_req.raise_for_status()
w_data = my_req.json()
main_data = w_data['list'][0:4]
w_details = [ item['weather'] for item in main_data]
w_conditions = [ item[0]['id'] for item in w_details ]

send_condition = False

for condition in w_conditions:
    ## Check the weather is rainy
    if condition < 700:
        send_condition = True

if send_condition:
    client = Client(MY_SID, MY_TOKEN)

    message = client.messages.create(
                     body="Bring an Umbrella",
                     from_= MY_NUMBER,
                     to='reciever-phone-number'
                       )