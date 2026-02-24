import pandas as pd 
import numpy as np


data = pd.read_csv("dataset.csv")

# print(data.info())

# check for missing values #

for col in data.columns:
    if data[col].isnull().any():
        print(f"Coulumn {col} has missing values")
        if pd.api.types.is_numeric_dtype(data[col]):
            data[col] = data[col].fillna(data[col].mean())
        else:
            data = data.dropna()

        
data = data[data["key"] != -1]

#seconds calculator: 1 milisecond * 1000 = 1 second
data["duration_s"] = data["duration_ms"]/1000
data = data.drop(columns = ["duration_ms"])



data = data.iloc[:, 2:]

# print(data.info())

        
# data.to_csv("spotify_data.csv", index = 0)
updated_data = pd.read_csv("spotify_data.csv")
print(updated_data.info())
