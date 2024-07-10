import requests
import pandas as pd

url = ' https://data.cityofnewyork.us/resource/dpec-ucu7.json'
params = {'$$app_token': '3n24PhVfrGN0jpYvSlbkFd7M3', 'rows': 3000}
re = requests.get(url, params=params)

data = re.json()
print(data)
