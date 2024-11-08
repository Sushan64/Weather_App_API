import requests
city_name = input("Enter City Name: ").capitalize()
api = input("Your Open Weather API: ")
def api_feching():
  url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={api}"
  response = requests.get(url)
  data = response.json()

  if data["cod"] == 200:
    city = data["name"]
    temp = data["main"]["temp"]
    feel_like = data["main"]["feels_like"]
    wind_speed = data["wind"]["speed"]
    wind_deg = data["wind"]["deg"]
    description= data["weather"][0]["description"]
    
    return city, temp, feel_like, wind_speed, wind_deg, description
  else:
    raise Exception("Couldn't Fetch Your data")



try:
  city, temp, feel_like, wind_speed, wind_deg, description = api_feching()
  print(f"City: {city} \nTemperature: {int(temp)}°C \nFeel Like: {int(feel_like)}°C \nWind Speed: {wind_speed} km/h \nWind Degree: {wind_deg}° \nWeather: {description}")
except Exception as e:
  print(str(e))
