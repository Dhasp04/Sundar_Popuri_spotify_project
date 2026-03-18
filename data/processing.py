import pandas as pd 
import numpy as np


data = pd.read_csv("dataset.csv")
data = data.iloc[:, 1:]

# print(data.info())

# check for missing values #

for col in data.columns:
    if data[col].isnull().any():
        # print(f"Coulumn {col} has missing values")
        if pd.api.types.is_numeric_dtype(data[col]):
            data[col] = data[col].fillna(data[col].mean())
        else:
            data = data.dropna(subset=[col])

# seconds calculator: 1 milisecond * 1000 = 1 second #
data["duration_s"] = data["duration_ms"]/1000
data = data.drop(columns = ["duration_ms"])



data = data.drop_duplicates(subset = ["track_id"], keep = "first")

def unique_list(series):
    return sorted(series.dropna().astype(str).unique().tolist())

agg_map = {}

for col in data.columns:
    if col == "track_id":
        continue
    if pd.api.types.is_numeric_dtype(data[col]):
        agg_map[col] = "mean"
    else:
        agg_map[col] = unique_list

processed = data.groupby("track_id", as_index=False).agg(agg_map)
processed = processed[data.columns.tolist()]
# print(processed.info())

        
processed.to_csv("spotify_data.csv", index = 0)
