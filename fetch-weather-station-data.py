import requests
from credentials import username, password

# login to get session id
weather_station_id = 184

login_url = f'http://sensornetwerk.inagro.be/Login.aspx?sensorId={weather_station_id}'

credentials = {
    'ctl00$ContentPlaceHolder1$Login1$UserName': username,
    'ctl00$ContentPlaceHolder1$Login1$Password': password}

r = requests.post(login_url, credentials)

session_id = r.cookies['ASP.NET_SessionId']

if session_id:
    print(f'logged in to weather station {weather_station_id} as {username}')
else:
    print('could not login')
    
# download
export_id = 'export_74e3415958304c48a98553b7e20f4e87'
export_filename = 'weather-station-data'
download_url = f'http://sensornetwerk.inagro.be/Download.aspx?id={export_id}&exportNaam={export_filename}'

cookie = f'ASP.NET_SessionId={session_id}'

download = requests.get(download_url, headers = {'Cookie': cookie})

print(f'downloaded data to file {export_filename}')

# write to file
