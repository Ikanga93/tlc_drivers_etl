# Import necessary libraries and modules
from extract import extract_data
import pandas as pd
import json

# Function to transform the extracted data
def transform_data(data):
    # Convert the json_data to a pandas dataframe
    # json_data = json.load(data)
    df = pd.DataFrame(data)
    # logging.info('Data transformed successfuly')

    # Fix column names
    df = df.rename(columns={ 
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
    print(df)            
    # Configure pandas to display all rows and columns
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
                
    return data

