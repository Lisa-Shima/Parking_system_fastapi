import requests
import pandas as pd

parking_lots_api = "http://localhost:8000/parking-lots"
parking_lots_id1_api = "http://localhost:8000/parking-lots/1"

def fetchdata(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

#Fetch data from the APIs
parking_lots_data = fetchdata(parking_lots_api)
parking_lots_id1_data = fetchdata(parking_lots_id1_api)

print(parking_lots_data)
print(parking_lots_id1_data) # Assuming parking_lots data is available

#Create dataframes from the fetched data
parking_lots_df = pd.DataFrame(parking_lots_data)
parking_lots_id1_df = pd.DataFrame(parking_lots_id1_data)


print("Parking_lots dataframe:")
print(parking_lots_df.head()) #prints first 5 rows of parking_lots dataframe
print(parking_lots_df.info()) 
print("parking_lots_1 dataframe:")
print(parking_lots_id1_df.head()) #prints rows of parking_lots_id1 dataframe
print(parking_lots_id1_df.info())

merged_df = pd.merge(
    parking_lots_df,
    parking_lots_id1_df,
    left_on ="id",
    right_on= "parking_lot_id",
    how="inner" #too include only matching rows
)

print("Merged dataframe:")
print(merged_df)
print(merged_df.info())

#preprocessing the data
print("Null values in parking_lots")
print(parking_lots_df.isnull().sum())

print("Null values in parking_lot_id1")
print(parking_lots_id1_df.isnull().sum(axis=0))

parking_lots_id1_df["name"].fillna("Unknown",inplace=True)


# parking_lots_df.dropna(inplace=True) 
parking_lots_df.dropna(inplace=True)

print(parking_lots_id1_df.isnull())
print(parking_lots_id1_df)
print(parking_lots_df.head())


# print(merged_df.dtypes)
print(parking_lots_df['name'].dtypes)
parking_lots_df['name'] = pd.to_datetime(parking_lots_df['name'],errors='coerce')
print(parking_lots_df.dtypes)


#Standadize data
parking_lots_df['name'] = parking_lots_df['name'].str.strip().str.title()
parking_lots_df['name'] = parking_lots_df['name'].str.strip().str.upper()

print(parking_lots_df['name'])

#Feature Engineering 
parking_lots_df["time"] = (parking_lots_df['beginning_time'] - parking_lots_df['ending_time']).dt.days//365
print(parking_lots_df['time'])

parking_lots_id1_df["parking_lot_time"] = pd.to_datetime(parking_lots_id1_df['parking_lot_time'],errors='coerce')
parking_lots_id1_df['parking_lot_hour'] = parking_lots_id1_df['parking_lot_hour'].dt.hour
parking_lots_id1_df['parking_lot_minute'] = parking_lots_id1_df['parking_lot_minute'].dt.minute

print(parking_lots_id1_df.head())



#remernging data after preprocessing 
merged_df = pd.merge(
 parking_lots_df,
 parking_lots_id1_df,
 left_on="id",
 right_on="parking_lot_id",
 how="outer")

#removing the irrelevant data fromthe dataframes

print("merged dataframe after data preprocessing") 
merged_df.drop(columns=["parking_lot_hour", "parking_lot_minute"], inplace= True)
print(parking_lots_df)
print(merged_df.head())

print(merged_df.info())
print(merged_df.isnull())

#normalization of data

numeric_columns = merged_df.select_dtypes(include=['int64','float64']).columns
print(numeric_columns)

from sklearn import MinMaxScaler
scale = MinMaxScaler()
merger_df = scaler.fit_transform(merger_df['time'])
print(merger_df['time'])