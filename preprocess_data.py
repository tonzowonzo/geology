# Import libraries.
import os
import cv2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = r"C:/Users/Tim/Desktop/BOKU/GIS/geology/geology/data/geological/ofr20051294/deposit.csv"
def preprocess_geological_data(data):
    df = pd.read_csv(data)
    df["main_mineral_list"] = df["commodity"].str.split(",")
    df["main_mineral"] = df["main_mineral_list"].str[0]
    df["label"] = df["main_mineral"] + "_" + df["dep_type"]
    print(df.head())
    return df
df = preprocess_geological_data(data)
commodities = df["label"].values
uniques, unique_counts = np.unique(commodities, return_counts=True)

for i, unique in enumerate(sorted(uniques)):
    print(f"Type: {unique}, Count: {unique_counts[i]}")