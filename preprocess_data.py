# Import libraries.
import os
import cv2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = r"C:/Users/Tim/Desktop/BOKU/GIS/geology/geology/data/geological/ofr20051294/deposit.csv"
def preprocess_geological_data(data, visualise=True):
    df = pd.read_csv(data)
    df["is_volcanic"] = False
    df["is_seismic"] = False
    df["main_mineral_list"] = df["commodity"].str.split(",")
    df["main_mineral"] = df["main_mineral_list"].str[0]
    df["label"] = df["main_mineral"] + "_" + df["dep_type"]
    if visualise:
        plt.figure(figsize=(12, 12))
        plt.scatter(df["longitude"].values, df["latitude"].values)
        plt.show()
    print(df.head())
    return df

df = preprocess_geological_data(data)
#commodities = df["label"].values
#uniques, unique_counts = np.unique(commodities, return_counts=True)

#for i, unique in enumerate(sorted(uniques)):
#    print(f"Type: {unique}, Count: {unique_counts[i]}")
    
def preprocess_seismic_data(data, visualise=True):
    df =  pd.read_csv(data)
    df[df["Type"] == "Earthquake"]
    df = df[["Latitude", "Longitude"]]
    df.columns = ["Earthquake Lat", "Earthquake Long"]
    if visualise:
        plt.figure(figsize=(12, 12))
        plt.scatter(df["Earthquake Long"].values, df["Earthquake Lat"].values)
        plt.show()
    return df


    

earthquake_data = "data/seismic/database.csv"
earthquake_df = preprocess_seismic_data(earthquake_data)


def make_final_df(ore_df, seismic_df, volcanic_df):
    df = ore_df.copy()
    for i in df.index:
        if i % 500 == 0:
            print(f"Iteration number: {i}")
        seismic = seismic_df.copy()
        lat_diff = abs(seismic["Earthquake Lat"] - df["latitude"][i])  <= 5
        long_diff = abs(seismic["Earthquake Long"] - df["longitude"][i])  <= 5
        if lat_diff[long_diff].any():
            df["is_seismic"][i] = True
            
    return df
        
df = make_final_df(df, earthquake_df, "test")

plt.style.use("dark_background")
plt.figure(figsize=(12, 12))
plt.scatter(df["longitude"].values, df["latitude"].values,
            c=df["is_seismic"].values, cmap="cool")
plt.scatter(earthquake_df["Earthquake Long"], earthquake_df["Earthquake Lat"],
            c="gray", alpha=0.2)
plt.xlabel("Latitude")
plt.ylabel("Longitude")
plt.legend(["Non-seismic", "Earthquake", "Seismic"])
plt.title("Is the area seismically active?")
plt.show()