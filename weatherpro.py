
'''import requests 
API_KEY = "185c9b57ac7cccf485ad420ec081ef7a"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}" 
response = requests.get(request_url)
if response.status_code == 200:
    data = response.json()
    weather = data['weather' ][0][ ' description' ]
    temperature = round(data["main"]["temp"]-273.15,2)
    print("Weather: ",weather)
    print("Temperature:",temperature, "celsius")
else:
    print("An error occured.")

'''
import requests
import json
print("Are you excited to know how the weather is?")
city=input("Enter the name of the city\n")
url=f"https://api.weatherapi.com/v1/current.json?key=199d6a14613d4435ad8191217232503&q={city}"
r=requests.get(url)
#Chennaiprint(r.text)
wdic=json.loads(r.text)
print(wdic["current"]["temp_c"])
