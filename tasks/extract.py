# Import necessary libraries and modules
import json
from sodapy import Socrata
from config import load_config

# Load the configuration file
config = load_config("/Users/jbshome/Desktop/tlc_drivers_etl/configurations/config.json")

# Function to extract data
def extract_data(*args):
    #config = load_config("/Users/jbshome/Desktop/tlc_drivers_etl/configurations/config.json", "r")
    client = Socrata(*args)

    results = client.get('dpec-ucu7', limit=3621)
    # df = pd.DataFrame.from_records(results)
    return results

if __name__ == "__main__":
    extracted_data = extract_data(config["tlc_api_url"] , config["tlc_app_token"], config["tlc_username"], config["tlc_password"])
    print(extracted_data)