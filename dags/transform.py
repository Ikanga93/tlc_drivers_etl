# Import necessary libraries and modules
from extract import extract_data
from config import load_config
import pandas as pd
import json

extracted_data = extract_data()
# Function to transform the extracted data
def transform_data(data):
    # Convert the json_data to a pandas dataframe
    # df = pd.DataFrame(data)
    # df = pd.json_normalize(data)
    # logging.info('Data transformed successfuly')

    # Fix column names
    df = data.rename(columns={ 
        'app_date':'application_date', 
        'lastupdate':'last_update'
    })
    # logging.info('Columns renamed successfully')
                
    # Drop some uneccessary columns 
    df = df.drop(['fru_interview_scheduled', 
                'wav_course', 'drug_test', 
                'defensive_driving', 
                'driver_exam', 
                'medical_clearance_form'], axis=1)
               
    # Configure pandas to display all rows and columns
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
                
    return df

# if __name__ == "__main__":
    # config = load_config("/Users/jbshome/Desktop/tlc_drivers_etl/configurations/config.json")
    # extracted_data = extract_data()
# print(transform_data(extracted_data)) 
    # print(transformed_data)