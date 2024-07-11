# Import necessary libraries and modules
from extract import extract_data
from config import load_config
import pandas as pd
import json
import logging

logging.BasicConfig(filename='extract.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# Function to transform the extracted data
def transform_data(df):
    df = df.rename(columns={ 
        'app_date':'application_date', 
        'lastupdate':'last_update'
    })
    # Drop some uneccessary columns 
    df = df.drop(['fru_interview_scheduled', 
                'wav_course', 'drug_test', 
                'defensive_driving', 
                'driver_exam', 
                'medical_clearance_form'], axis=1)
                
    return df

# if __name__ == "__main__":
    # config = load_config("/Users/jbshome/Desktop/tlc_drivers_etl/configurations/config.json")
extracted_data = extract_data()
transform_data(extracted_data)

print(transform_data)