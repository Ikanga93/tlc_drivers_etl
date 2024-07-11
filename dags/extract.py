# Import necessary libraries and modules
import json
import requests
import pandas as pd
# from sodapy import Socrata
# from config import load_config

# Load the configuration file
# config = load_config("/Users/jbshome/Desktop/tlc_drivers_etl/config.json")

# Function to extract data
import requests
import pandas as pd

# url = 'https://data.cityofnewyork.us/resource/dpec-ucu7.json?'
# params = {'$$app_token': '3n24PhVfrGN0jpYvSlbkFd7M3'}

def extract_data():
    url = 'https://data.cityofnewyork.us/resource/dpec-ucu7.json'
    # params = {'$$app_token': '3n24PhVfrGN0jpYvSlbkFd7M3'}
    re = requests.get(url)
    data = re.json()
    '''
    client = Socrata(config["tlc_api_url"],
                    config["tlc_app_token"], 
                    config["tlc_username"], 
                    config["tlc_password"])

    results = client.get('dpec-ucu7', limit=4000)
    '''
    return data

if __name__ == "__main__":
    extracted_data = extract_data()
    print(extracted_data)
