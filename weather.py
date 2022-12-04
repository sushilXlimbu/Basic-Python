import requests

API_KEY = "14305d36e61f4891083714c9d102d158"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter your city: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print("Today\'s weather is",weather)
    temp = round(data['main']['temp'] - 273.15, 2 )
    print('Today\'s temperature will be',temp,'*C') 
    
else:
    print('error 404 not found')
