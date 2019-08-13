import requests
import os.path
from credentials import username, password

# login

weather_station_id = 184

login_url = f'http://sensornetwerk.inagro.be/Login.aspx?sensorId={weather_station_id}'

credentials = {
    'ctl00$ContentPlaceHolder1$Login1$UserName': username,
    'ctl00$ContentPlaceHolder1$Login1$Password': password}

login = requests.post(login_url, credentials)

print(dict(login.cookies))