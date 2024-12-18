import requests
import pandas as pd

try:
    parking_lot_api = requests.get('http://127.0.0.1:8000/parking-lots')
    parking_lot_api.raise_for_status()
    parking_lot_api_data = parking_lot_api.json()
    # print(parking_lot_api_data)
    
    parking_lot_id_api = requests.get('http://127.0.0.1:8000/parking-lots/1')
    parking_lot_id_api.raise_for_status()
    parking_lot_id_api_data = parking_lot_id_api.json()
    print('\nWith ID: ')
    # print(parking_lot_id_api_data)
    
    pldf = pd.DataFrame(parking_lot_api_data)
    # print(pldf)
    plidf = pd.DataFrame([parking_lot_id_api_data])
    # print(plidf)
    
    inner_merged_df = pd.merge(pldf, plidf, on = "id", how = "inner")
    print(inner_merged_df.head())
    print(inner_merged_df.isnull().sum())
    print(inner_merged_df.dtypes)
    
    inner_merged_df.ffill(inplace=True)

except requests.exceptions.RequestException as e:
    print(f"Error fetching data from API: {e}")
    print("Error: Unable to connect to the server")
    exit()
    
