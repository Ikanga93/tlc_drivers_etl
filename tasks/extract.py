# Import necessary libraries and modules
import pandas as pd
from sodapy import Socrata

# App token for the api
app_token = '3n24PhVfrGN0jpYvSlbkFd7M3'

client = Socrata('data.cityofnewyork.us',
                 app_token,
                 username='ekuke003@gmail.com',
                 password='D2racine4ac#')

results = client.get('dpec-ucu7', limit=3621)
results_df = pd.DataFrame.from_records(results)
print(results_df)