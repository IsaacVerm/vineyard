import requests, os.path
from credentials import username, password

# login

weather_station_id = 184

login_url = f'http://sensornetwerk.inagro.be/Login.aspx?sensorId={weather_station_id}'

credentials = {
    'ctl00$ContentPlaceHolder1$Login1$UserName': username,
    'ctl00$ContentPlaceHolder1$Login1$Password': password}

login = requests.post(login_url, credentials)

session_id = login.cookies['ASP.NET_SessionId']
network_token = login.cookies['.Sensornetwerk']

if session_id and network_token:
    print(f'logged in to weather station {weather_station_id} as {username}')
else:
    print('could not login')

# download

url = 'http://sensornetwerk.inagro.be/Download.aspx'
export_id = 'export_55d001947f4a4aa58844198cc2e912df'

querystring = {'id': export_id ,
               'exportNaam': 'weather-station-data'}

headers = {
    'Cookie': f'ASP.NET_SessionId={session_id}; .Sensornetwerk={network_token}',
}

response = requests.request("GET", url, headers=headers, params=querystring)

if response.content:
    print('downloaded data for all of 2019')
else:
    print('data could not be downloaded')

# write to file
output = open('test.xlsx', 'wb')
output.write(response.content)
output.close()

if os.path.isfile('test.xlsx'):
    print('data was saved as test.xlsx')
else:
    print('data could not be saved')
