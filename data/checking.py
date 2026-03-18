import pandas as pd

updated_data = pd.read_csv("spotify_data.csv")

print(updated_data.info())

print(updated_data["track_id"].size - updated_data["track_id"].nunique())